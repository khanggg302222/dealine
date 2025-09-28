var API_URL = "http://127.0.0.1:8000/users";
var editingUserId = null;

// Load all user and hiển thị
function loadUsers() {
    fetch(API_URL)
    .then(response => response.json()) 
    .then(users => {
        var table = document.getElementById("userTable");
        table.innerHTML = ""; // delete old table
// logic hiển thị data on table
        for (var i = 0; i < users.length; i++) {
            var user = users[i];

            var row = document.createElement("tr");

            var nameCell = document.createElement("td");
            nameCell.innerHTML = user.name;
            row.appendChild(nameCell);

            var emailCell = document.createElement("td");
            emailCell.innerHTML = user.email;
            row.appendChild(emailCell);

            var actionCell = document.createElement("td");

            // button edit 
            var editBtn = document.createElement("button");
            editBtn.innerHTML = "Edit";
            editBtn.className = "edit";
            editBtn.onclick = function() {
                editUser(user);
            };
            actionCell.appendChild(editBtn);

            // button delete 
            var deleteBtn = document.createElement("button");
            deleteBtn.innerHTML = "Delete";
            deleteBtn.className = "delete";
            deleteBtn.onclick = function() {
                deleteUser(user.id);
            };
            actionCell.appendChild(deleteBtn);

            row.appendChild(actionCell);
            table.appendChild(row);
        }
    });
}

// logic của máy cái button 
function addUser() {
    // put data in form
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;

    // check data input
    if (name === "" || email === "") {
        alert("Vui lòng nhập đầy đủ tên và email");
        return;
    }

    // creative object để post in server
    var data = { name: name, email: email,age:20 }; // thêm age tạm thời để chạy được api theo chuẩn định dạng fastapi !!!!!!!!!!!!!!!!!!!!!!! LỖI LỚN NHẤT PHẢI CHÚ Ý
                 
    // address post data
    fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        // post-processing after successfully sending the data
        document.getElementById("name").value = ""; // remove 
        document.getElementById("email").value = "";
        editingUserId = null; // remove status edit

        loadUsers();
    });
}
function editUser(user) {
    document.getElementById("name").value = user.name;
    document.getElementById("email").value = user.email;
    editingUserId = user.id;
}

function deleteUser(userId) {
    if (confirm("Bạn có chắc muốn xóa user này không?")) {
        fetch(API_URL + "/" + userId, { method: "DELETE" })
        .then(response => response.json())
        .then(result => {
            loadUsers(); 
        });
    }
}

// When page loads, automatically load users
window.onload = loadUsers;