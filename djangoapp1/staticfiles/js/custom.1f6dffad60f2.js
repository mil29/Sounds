// This js is for a progress bar for music upload page
const axios = import('axios');



function progressBar () {

    const uploadForm = document.getElementById('upload-form')
    const input = document.getElementById("id_track")
    const progressBox = document.getElementById('progress-box')
    const cancelBox = document.getElementById('cancel-box')
    const cancelBtn = document.getElementById('cancel-btn')
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    const progbar = document.getElementById('musicFormUpload')



    progressBox.classList.remove('not-visible');
    cancelBox.classList.remove('not-visible');

    const upload_data = input.files[0]
    const data = new FormData();

    data.append('csrfmiddlewaretoken', csrf[0].value);
    data.append('track', upload_data);

    const config = {
        onUploadProgress: function(progressEvent) {
        var percent = Math.round( (progressEvent.loaded * 100) / progressEvent.total );
        progressBox.innerHTML = `<h5 style="text-align:center;">${percent.toFixed(1)}%</h5>
                                            <div class="progress" style="height: 30px;">
                                            <div class="progress-bar bg-success" role="progressbar" style="width: ${percent}%" 
                                            aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>`

        }
    };
    axios.post('https://s3.console.aws.amazon.com/s3/buckets/sounds-connect-app?region=eu-west-2&prefix=media/path/to/audio/&showversions=false', data, config)
        .then(function (res) {
        progressBox.innerHTML = res.data;
        })
        .catch(function (err) {
        progressBox.innerHTML = err.message;
    });
};

