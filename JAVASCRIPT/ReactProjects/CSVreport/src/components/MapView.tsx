import React, { useEffect, useState, useCallback } from 'react';
import { GoogleMap, LoadScript, Polyline, Marker, Rectangle } from '@react-google-maps/api';

// Configurações do mapa
const mapContainerStyle = {
  width: '100%',
  height: '500px'
};

// Estilo Satélite (Google Earth)
const satelliteOptions = {
  zoomControl: true,
  tilt: 45, // Inclinação 3D como no Google Earth
  gestureHandling: 'auto',
  mapTypeControl: true,
  scaleControl: true,
  streetViewControl: true,
  rotateControl: true,
  fullscreenControl: true,
  mapTypeId: 'satellite', // Tipo de mapa satélite
  styles: [
    {
      "elementType": "geometry",
      "stylers": [{ "color": "#1d2c4d" }]
    },
    {
      "elementType": "labels.text.fill",
      "stylers": [{ "color": "#8ec3b9" }]
    },
    {
      "elementType": "labels.text.stroke",
      "stylers": [{ "color": "#1a3646" }]
    },
    {
      "featureType": "administrative",
      "elementType": "geometry",
      "stylers": [{ "visibility": "off" }]
    },
    {
      "featureType": "administrative.country",
      "elementType": "geometry.stroke",
      "stylers": [{ "color": "#4b6878" }]
    },
    {
      "featureType": "administrative.land_parcel",
      "stylers": [{ "visibility": "off" }]
    },
    {
      "featureType": "administrative.neighborhood",
      "stylers": [{ "visibility": "off" }]
    },
    {
      "featureType": "poi",
      "stylers": [{ "visibility": "off" }]
    },
    {
      "featureType": "poi",
      "elementType": "geometry",
      "stylers": [{ "color": "#283d6a" }]
    },
    {
      "featureType": "road",
      "stylers": [{ "visibility": "off" }]
    },
    {
      "featureType": "transit",
      "stylers": [{ "visibility": "off" }]
    },
    {
      "featureType": "water",
      "elementType": "geometry",
      "stylers": [{ "color": "#0e1626" }]
    },
    {
      "featureType": "water",
      "elementType": "labels.text.fill",
      "stylers": [{ "color": "#4e6d70" }]
    }
  ]
};

// Estilo da linha de voo
const polylineOptions = {
  strokeColor: '#00FF00', // Verde para melhor contraste
  strokeOpacity: 0.9,
  strokeWeight: 4,
  fillColor: '#00FF00',
  fillOpacity: 0.3,
};

// Estilo do retângulo da área
const rectangleOptions = {
  strokeColor: '#FFFF00',
  strokeOpacity: 0.8,
  strokeWeight: 3,
  fillColor: '#FFFF00',
  fillOpacity: 0.1,
};

const MapView = ({ csv }) => {
  const [flightPath, setFlightPath] = useState([]);
  const [mapBounds, setMapBounds] = useState(null);
  const [mapCenter, setMapCenter] = useState({ lat: -23.2557, lng: -47.2987 });
  const [mapLoaded, setMapLoaded] = useState(false);

  // Sua API Key do Google Maps
  const GOOGLE_MAPS_API_KEY = '';

  useEffect(() => {
    if (!csv || !csv.data || csv.data.length === 0) {
      console.log('CSV data not available or empty');
      return;
    }

    try {
      // Extrair coordenadas do CSV - ajuste os índices conforme necessário
      const coordinates = csv.data
        .filter(row => row[2] && row[3] && !isNaN(parseFloat(row[2])) && !isNaN(parseFloat(row[3])))
        .map(row => ({
          lat: parseFloat(row[2]),
          lng: parseFloat(row[3])
        }));

      if (coordinates.length === 0) {
        console.log('No valid coordinates found');
        return;
      }

      console.log('Coordinates extracted:', coordinates.length);

      // Calcular bounding box da área do voo
      const lats = coordinates.map(coord => coord.lat);
      const lngs = coordinates.map(coord => coord.lng);

      const bounds = {
        north: Math.max(...lats),
        south: Math.min(...lats),
        east: Math.max(...lngs),
        west: Math.min(...lngs)
      };

      // Adicionar uma pequena margem aos bounds
      const margin = 0;
      const boundedBounds = {
        north: bounds.north + margin,
        south: bounds.south - margin,
        east: bounds.east + margin,
        west: bounds.west - margin
      };

      // Calcular centro do mapa
      const centerLat = (bounds.north + bounds.south) / 2;
      const centerLng = (bounds.east + bounds.west) / 2;

      setFlightPath(coordinates);
      setMapBounds(boundedBounds);
      setMapCenter({ lat: centerLat, lng: centerLng });

    } catch (error) {
      console.error('Error processing coordinates:', error);
    }
  }, [csv]);

  // Callback quando o mapa carrega
  const onMapLoad = useCallback((map) => {
    setMapLoaded(true);
    console.log('Google Maps loaded successfully');
  }, []);

  // Callback se houver erro no carregamento
  const onLoadError = (error) => {
    console.error('Error loading Google Maps:', error);
  };

  return (
    <div className="google-map-view">      
      <LoadScript 
        googleMapsApiKey={GOOGLE_MAPS_API_KEY}
        onError={onLoadError}
      >
        <GoogleMap
          mapContainerStyle={mapContainerStyle}
          center={mapCenter}
          zoom={20}
          options={satelliteOptions}
          onLoad={onMapLoad}
        >
          {/* Linha do trajeto do drone */}
          {flightPath.length > 0 && (
            <Polyline
              path={flightPath}
              options={polylineOptions}
            />
          )}

          {/* Retângulo da área de voo */}
          {mapBounds && (
            <Rectangle
              bounds={mapBounds}
              options={rectangleOptions}
            />
          )}

          {/* Marcador do ponto inicial */}
          {flightPath.length > 0 && (
            <Marker
              position={flightPath[0]}
              icon={{url: "http://maps.google.com/mapfiles/ms/icons/green-dot.png"}}
              title="Ponto Inicial do Voo"
            />
          )}

          {/* Marcador do ponto final */}
          {flightPath.length > 0 && (
            <Marker
              position={flightPath[flightPath.length - 1]}
              icon={{url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"}}
              title="Ponto Final do Voo"
            />
          )}
        </GoogleMap>
      </LoadScript>

      {!mapLoaded && (
        <div style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          padding: '10px 20px',
          backgroundColor: 'rgba(255,255,255,0.9)',
          border: '1px solid #ccc',
          borderRadius: '4px',
          zIndex: 1000
        }}>
          Carregando Google Maps...
        </div>
      )}
    </div>
  );
};

export default MapView;