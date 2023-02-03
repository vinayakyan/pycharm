function validate_form(){
    dept_name = document.getElementById('exampleInputDepartment').value
    dept_loc = document.getElementById('exampleInputDepartmentLocation').value
    console.log(dept_loc.length)
    if(dept_name.length && dept_loc.length){
        return true
    }
    return false
}