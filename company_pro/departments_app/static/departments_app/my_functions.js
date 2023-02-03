function validate_pan(){
    const file = document.getElementById('exampleInputPan').value
    const extension = file.split('.')[1]
    if(extension && extension === 'pdf'){
        document.getElementById('errPan').innerHTML = ''
        return true
    }else{
        document.getElementById('errPan').innerHTML = 'Only Pdf Files Allowed'
        return false
    }
}

function validate_voter(){
    const file = document.getElementById('exampleInputVoter').value
    const extension = file.split('.')[1]
    if(extension && extension === 'pdf'){
        document.getElementById('errVoter').innerHTML = ''
        return true
    }else{
        document.getElementById('errVoter').innerHTML = 'Only Pdf Files Allowed'
        return false
    }
}

function validate_files(){
    if(validate_pan() && validate_voter()){
        document.getElementById('submit').disabled = false
    }else{
        document.getElementById('submit').disabled = true
    }
}

function validate_form(){
    const name = document.getElementById('exampleInputEmployee').value
    const dept = document.getElementById('exampleInputDepartment').value
    const desg = document.getElementById('exampleInputDesignation').value
    if(name.length && dept.length && desg.length && validate_pan() && validate_voter()){
        return true
    }else{
        return false
    }
}