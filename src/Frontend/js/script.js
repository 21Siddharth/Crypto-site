document.addEventListener("DOMContentLoaded", function () {
    toggleOptions();
});

function toggleOptions() {
    const method = document.getElementById('method').value;
    const shiftOption = document.getElementById('shift-option');
    const rot13Options = document.getElementById('rot13-options');

    if (method === 'caesar') {
        shiftOption.style.display = 'block';
        rot13Options.style.display = 'none';
    } else if (method === 'rot13') {
        shiftOption.style.display = 'none';
        rot13Options.style.display = 'block';
    } else {
        shiftOption.style.display = 'none';
        rot13Options.style.display = 'none';
    }
}

function encodeText() {
    const text = document.getElementById('text').value;
    const shift = document.getElementById('shift').value;
    const method = document.getElementById('method').value;
    const encodeNumbersCaesar = document.getElementById('encode-numbers-caesar').checked;

    const rotateUppercase = document.getElementById('rotate-uppercase').checked;
    const rotateLowercase = document.getElementById('rotate-lowercase').checked;
    const rotateNumbers = document.getElementById('rotate-numbers').checked;

    const requestData = {
        text: text,
        shift: shift,
        method: method,
        encodeNumbersCaesar: encodeNumbersCaesar,
        rotateUppercase: rotateUppercase,
        rotateLowercase: rotateLowercase,
        rotateNumbers: rotateNumbers
    };

    fetch('/encode', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Encoded Text: ' + data.encoded_text;
    });
}

function decodeText() {
    const text = document.getElementById('text').value;
    const shift = document.getElementById('shift').value;
    const method = document.getElementById('method').value;
    const encodeNumbersCaesar = document.getElementById('encode-numbers-caesar').checked;

    const rotateUppercase = document.getElementById('rotate-uppercase').checked;
    const rotateLowercase = document.getElementById('rotate-lowercase').checked;
    const rotateNumbers = document.getElementById('rotate-numbers').checked;

    const requestData = {
        text: text,
        shift: shift,
        method: method,
        encodeNumbersCaesar: encodeNumbersCaesar,
        rotateUppercase: rotateUppercase,
        rotateLowercase: rotateLowercase,
        rotateNumbers: rotateNumbers
    };

    fetch('/decode', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Decoded Text: ' + data.decoded_text;
    });
}
