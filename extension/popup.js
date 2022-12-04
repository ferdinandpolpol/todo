
document.addEventListener("DOMContentLoaded", function () {

    var getUsers = async () => {
        let response = await fetch("http://127.0.0.1:8000/all_users")
        let users = await response.json()
        console.log(users)

        let select = document.getElementById("userSelect")
        for (user of users) {
            let newOption = document.createElement('option')
            newOption.text = user.username
            newOption.value = user.id
            select.add(newOption)
        }
    }
    getUsers()

    document.getElementById("todoForm").addEventListener("submit", async () => {
        let formData = new FormData()
        let userSelect = document.getElementById("userSelect")
        formData.append("author", userSelect.value)
        formData.append("title", document.getElementById("title").value)
        formData.append("completed", document.getElementById("completed").checked)

        await fetch("http://127.0.0.1:8000/", {
            method: "POST",
            body: formData
        })
    })
});