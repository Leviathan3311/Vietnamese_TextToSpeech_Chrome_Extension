const form = document.getElementById('news-form');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const input = document.getElementById('news-text').value;
    const voice = document.getElementById('voice-select').value;
    const loadingMessage = document.getElementById('loading-message');
    const resultDiv = document.getElementById('prediction-result');

    // Hiển thị thông báo đang chờ
    loadingMessage.style.display = 'block';
    resultDiv.innerText = '';

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: input, voice: voice }),
        });

        // Ẩn thông báo khi nhận được phản hồi
        loadingMessage.style.display = 'none';

        if (response.ok) {
            const jsonResponse = await response.json();

            if (jsonResponse.output_audio) {
                // Tạo URL với tham số ngẫu nhiên để tránh cache
                const audioUrl = `${jsonResponse.output_audio}?t=${new Date().getTime()}`;

                // Tạo phần tử audio và phát
                const audio = new Audio(audioUrl);
                audio.play();

                resultDiv.innerText = 'Âm thanh đã được tạo và đang phát...';
            } else {
                resultDiv.innerText = 'Không tạo được âm thanh';
            }
        } else {
            console.error('Request failed:', response.status);
            resultDiv.innerText = 'Không thể tạo âm thanh.';
        }
    } catch (error) {
        console.error('Request failed:', error);
        resultDiv.innerText = 'Đã xảy ra lỗi trong quá trình xử lý yêu cầu.';
    }
});
