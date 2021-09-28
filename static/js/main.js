const URL = '/trans/';
let div = document.createElement('div');
div.id = 'messages';
let start = document.createElement('button');
start.id = 'start';
start.innerHTML = 'Start';
let stop = document.createElement('button');
stop.id = 'stop';
stop.innerHTML = 'Stop';
document.querySelector('#foiceRec').appendChild(div);
document.querySelector('#foiceRec').appendChild(start);
document.querySelector('#foiceRec').appendChild(stop);
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
