const URL = '/trans/';
let div = document.createElement('div');
div.id = 'messages';
let start = document.createElement('button');
start.id = 'start';

let stop = document.createElement('button');
stop.id = 'stop';
start.innerHTML = `<svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M45.92 28.9224C45.92 27.8024 45.0635 26.9459 43.9435 26.9459C42.8235 26.9459 41.967 27.8024 41.967 28.9224C41.967 36.6306 35.7082 42.8894 28 42.8894C20.2917 42.8894 14.0329 36.6306 14.0329 28.9224C14.0329 27.8024 13.1765 26.9459 12.0565 26.9459C10.9365 26.9459 10.08 27.8024 10.08 28.9224C10.08 38.08 16.9318 45.7882 26.0235 46.7765V52.0471H18.8423C17.7223 52.0471 16.8659 52.9035 16.8659 54.0235C16.8659 55.1435 17.7223 56 18.8423 56H37.1576C38.2776 56 39.1341 55.1435 39.1341 54.0235C39.1341 52.9035 38.2776 52.0471 37.1576 52.0471H29.9765V46.7765C39.0682 45.7882 45.92 38.08 45.92 28.9224Z" fill="black"/>
<path d="M28 0C21.9388 0 16.9976 4.94118 16.9976 11.0024V28.8565C16.9976 34.9835 21.9388 39.8588 28 39.9247C34.0611 39.9247 39.0023 34.9835 39.0023 28.9224V11.0024C39.0023 4.94118 34.0611 0 28 0Z" fill="black"/>
</svg>`;
stop.innerHTML = `<svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M45.92 28.9224C45.92 27.8024 45.0635 26.9459 43.9435 26.9459C42.8235 26.9459 41.967 27.8024 41.967 28.9224C41.967 36.6306 35.7082 42.8894 28 42.8894C20.2917 42.8894 14.0329 36.6306 14.0329 28.9224C14.0329 27.8024 13.1764 26.9459 12.0564 26.9459C10.9364 26.9459 10.08 27.8024 10.08 28.9224C10.08 38.08 16.9317 45.7882 26.0235 46.7765V52.0471H18.8423C17.7223 52.0471 16.8658 52.9035 16.8658 54.0235C16.8658 55.1435 17.7223 56 18.8423 56H37.1576C38.2776 56 39.1341 55.1435 39.1341 54.0235C39.1341 52.9035 38.2776 52.0471 37.1576 52.0471H29.9764V46.7765C39.0682 45.7882 45.92 38.08 45.92 28.9224Z" fill="#59BECC"/>
<path d="M28 0C21.9389 0 16.9977 4.94118 16.9977 11.0024V28.8565C16.9977 34.9835 21.9389 39.8588 28 39.9247C34.0612 39.9247 39.0024 34.9835 39.0024 28.9224V11.0024C39.0024 4.94118 34.0612 0 28 0Z" fill="#59BECC"/>
</svg>`
document.querySelector('#foiceRec').appendChild(div);
document.querySelector('#foiceRec').appendChild(start);
document.querySelector('#foiceRec').appendChild(stop);
stop.style.display = 'none'
start.addEventListener('click', function() {
    start.style.display = 'none'
    stop.style.display = 'block'
})
stop.addEventListener('click', function() {
    stop.style.display = 'none'
    start.style.display = 'block'
})
navigator.mediaDevices.getUserMedia({ audio: true})
    .then(stream => {
        const mediaRecorder = new MediaRecorder(stream);

        document.querySelector('#start').addEventListener('click', function(){
            mediaRecorder.start();
        });
        let audioChunks = [];
        mediaRecorder.addEventListener("dataavailable",function(event) {
            audioChunks.push(event.data);
        });

        document.querySelector('#stop').addEventListener('click', function(){
            mediaRecorder.stop();
        });

        mediaRecorder.addEventListener("stop", function() {
            const audioBlob = new Blob(audioChunks, {
                type: 'audio/wav;codecs=pcm'
            });

            let fd = new FormData();
            fd.append('voice', audioBlob);
            sendVoice(fd);
            audioChunks = [];
        });
    });

async function sendVoice(form) {
    let promise = await fetch(URL, {
        method: 'POST',
        body: form});
    if (promise.ok) {
        let response =  await promise.json();
        console.log(response.data);
        let audio = document.createElement('audio');
        audio.src = response.data;
        audio.controls = true;
        audio.autoplay = true;
        document.querySelector('#messages').appendChild(audio);
    }
}

// Typing
let typingContainer = document.querySelector('#typingText')

let typewriter = new Typewriter(typingContainer, {
    loop: true,
    delay: 75,
});
  
typewriter
    .pauseFor(100)
    .typeString('Выберите язык')
    .pauseFor(2500)
    .deleteChars(13)
    .typeString('Select a language')
    .pauseFor(2500)
    .deleteChars(17)
    .typeString('Tildi tańdańyz')
    .pauseFor(2500)
    .start();

// Select lenguage
selectKazahstan.addEventListener('click', function(){
    selectLenguage.style.display = "none";
    app.style.display = "block";
 
    document.querySelector('#languageKZ').style.color = "#59BECC"
    document.querySelector('.hint-title').append('Sálem');
    document.querySelector('.hint-subtitle').append('Bul qalaı jumys isteıdi ?');

    document.querySelector('.hint-one').append('Mıkrofondy basyńyz');
    document.querySelector('.hint-two').append('"Sálem Oleg" dep aıtyńyz jáne ol sizge bárin aıtady');
    document.querySelector('.hint-three').append('Eger ýaqyt bolmasa, "Oleg [sózdi] [aǵylshyn] tiline aýdaryńyz" dep aıtyńyz.');
});

selectRussian.addEventListener('click', function(){
    selectLenguage.style.display = "none";
    app.style.display = "block";

    document.querySelector('#languageRU').style.color = "#59BECC"
    document.querySelector('.hint-title').append('Привет');
    document.querySelector('.hint-subtitle').append('Как это работает ?');

    document.querySelector('.hint-one').append('Нажимай на микрофон');
    document.querySelector('.hint-two').append('Скажи "Привет Олег" и он тебе сам все расскажет');
    document.querySelector('.hint-three').append('Если нет времени, просто скажи "Олег переведи [слово] на [английский язык]"');
});

selectEngl.addEventListener('click', function(){
    selectLenguage.style.display = "none";
    app.style.display = "block";

    document.querySelector('#languageUS').style.color = "#59BECC"
    document.querySelector('.hint-title').append('Hello');
    document.querySelector('.hint-subtitle').append('How does it work?');

    document.querySelector('.hint-one').append('Press the microphone');
    document.querySelector('.hint-two').append('Say "Hi Oleg" and he\'\ll tell you all about it.');
    document.querySelector('.hint-three').append('If there is no time, just say "Oleg, translate [word] into [English].');
});
