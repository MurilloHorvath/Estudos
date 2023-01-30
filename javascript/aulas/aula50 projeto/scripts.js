function addTask() {

    const taskTitle = document.querySelector("#task-title").value

    if(taskTitle) {
        // clona template
        const template = document.querySelector(".template")
        const newTask = template.cloneNode(true)
        // adiciona titulo
        newTask.querySelector(".task-title").textContent = taskTitle
        // remover as classes desnecessarias
        newTask.classList.remove("template")
        newTask.classList.remove("hide")
        // adiciona tarefa na lista
        const list = document.querySelector("#task-list")
        list.appendChild(newTask)

        // adicionar evento de remover
        const removeBtn = newTask.querySelector(".remove-btn").addEventListener("click", function(){
            removeTask(this)
        })

        // adicioanr evento de completar tarefa
        const doneBtn = newTask.querySelector(".done-btn").addEventListener("click", function() {
            completeTask(this)
        })

        // lispar texto
        document.querySelector("#task-title").value = ""

    }

}

// função de remover a tarefa
function removeTask(task) {
    task.parentNode.remove(true)
}

// função de completar a tarefa
function completeTask(task) {
    const taskComplete = task.parentNode

    taskComplete.classList.toggle("done")
}

// evento de adicionar tarefa
const addBtn = document.querySelector("#add-btn")

addBtn.addEventListener("click", function(e) {

    e.preventDefault()

    addTask()

})