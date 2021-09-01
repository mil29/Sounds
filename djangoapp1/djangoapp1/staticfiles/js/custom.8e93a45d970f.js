// This js is for a progress bar for music upload page

function progressBar() {
    setTimeout(function () {

    const uploadForm = document.getElementById('upload-form')
    const input = document.getElementById("id_track")
    const progressBox = document.getElementById('progress-box')
    const cancelBox = document.getElementById('cancel-box')
    const cancelBtn = document.getElementById('cancel-btn')
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    const progbar = document.getElementById('musicFormUpload')


        progressBox.classList.remove('not-visible')
        cancelBox.classList.remove('not-visible') 
    
            const upload_data = input.files[0]
            const url = URL.createObjectURL(upload_data)
            // console.log(upload_data);
        
        const fd = new FormData()
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('track', upload_data)
    
        $.ajax({
            type: 'POST',
            contentType: 'multipart/form-data',
            data: fd,
            url: 'https://s3.console.aws.amazon.com/s3/buckets/sounds-connect-app?region=eu-west-2&prefix=media/path/to/audio/&showversions=false',
            beforeSend: function(){
    
            },
            xhr: function(){
                const xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', e=>{
                    console.log(e);
                    if (e.lengthComputable) {
                        const percent = (e.loaded / e.total) * 100;
                        console.log(percent);
                        progressBox.innerHTML = `<h5 style="text-align:center;">${percent.toFixed(1)}%</h5>
                                                <div class="progress" style="height: 30px;">
                                                <div class="progress-bar bg-success" role="progressbar" style="width: ${percent}%" 
                                                aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
                                                </div>`
                    }
                })
                cancelBtn.addEventListener('click', ()=>{
                    xhr.abort()
                    progressBox.innerHTML=""
                    cancelBox.classList.add('not-visible')
                    window.location.reload();
                })
                return xhr;
            },
            success: function(response){
                // console.log(response);
                uploadForm.reset()
                cancelBox.classList.add('not-visible')
            },
            error: function(error){
                console.log(error);
            },
            cache: false,
            contentType: false,
            processData: false,
        })
    
    }, 400)

    }
