const uploadForm = document.getElementById('upload-form')
const input = document.getElementById('id_track')
console.log(uploadForm)
const progressBox = document.getElementById('progress-box')
const cancelBox = document.getElementById('cancel-box')
const cancelBtn = document.getElementById('cancel-btn')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

input.addEventListener('change', ()=> {
    progressBox.classList.remove('not-visible')
    cancelBox.classList.remove('not-visible')

    const upload_data = input.files[0]

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append(' ')
})

