 const selectImage = document.querySelector('.select-image');
        const inputFile = document.querySelector('#file');
        const imgArea = document.querySelector('.img-area');
        const downloadButton = document.querySelector('#downloadButton');

        selectImage.addEventListener('click', function () {
            inputFile.click();
        });

        inputFile.addEventListener('change', function () {
            const image = this.files[0];
            if (image.size < 2000000) {
                const reader = new FileReader();
                reader.onload = () => {
                    const allImg = imgArea.querySelectorAll('img');
                    allImg.forEach(item => item.remove());
                    const imgUrl = reader.result;
                    const img = document.createElement('img');
                    img.src = imgUrl;
                    imgArea.appendChild(img);
                    imgArea.classList.add('active');
                    imgArea.dataset.img = image.name;
                    downloadButton.style.display = 'block';
                };
                reader.readAsDataURL(image);
            } else {
                alert("Image size more than 2MB");
            }
        });

        downloadButton.addEventListener('click', function () {
            const imgSrc = imgArea.querySelector('img').src;
            const link = document.createElement('a');
            link.href = imgSrc;
            link.download = imgArea.dataset.img || 'image';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });