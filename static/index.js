window.addEventListener('DOMContentLoaded', () => {});

function validate(){
    var spinner = document.querySelector("#spin");
    spinner.style.display = 'block';
    var form = document.querySelector("#analyseform");
    var extension = form.excelFile.value.split('\\').pop().split('.').pop();
    var flash = document.querySelector("#flash");
    if (extension == "xlsx"){
        flash.className = "alert alert-success";
        flash.innerHTML = "File Valid! Your Graph Will be Available at Graphs Link";
    } else {
        flash.className = "alert alert-danger";
        flash.innerHTML = "File Invalid!!";
    }
    flash.style.display = 'block';
    // fetch('/emails', {
    // method: 'POST',
    // body: JSON.stringify({
    //     recipients: 'baz@example.com',
    //     subject: 'Meeting time',
    //     body: 'How about we meet tomorrow at 3pm?'
    // })
    // })
    // .then(response => response.json())
    // .then(result => {
    //     console.log(result);
    // });
    return extension == "xlsx";
}