import { useState, useEffect } from "react";

function Users() {
    const [users, setUsers] = useState([]); 

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => res.json())
      .then((data) => setUsers(data));
  }, []);

  return(
    <div>
        <h2>Users List</h2>
        <ul>
            {users.map((user) => (<li key={user.id}>{user.name}</li>))}
        </ul>
    </div>
  )
}

export default Users;