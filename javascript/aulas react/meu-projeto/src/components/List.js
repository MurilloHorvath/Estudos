import Item from './Item'

function List() {
    return (
        <>
            <h1>Minha Lista</h1>
            <ul>
                <Item marca="Ferrari" lancamento={1940} />
                <Item marca="Audi" lancamento={1909} />
                <Item marca="BMW" lancamento={1916} />
                <Item/>
            </ul>
        </>
    )
}

export default List