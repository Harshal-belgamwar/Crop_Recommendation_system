form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const city = document.getElementById('city').value;
    const area = document.getElementById('area').value;
    const temp = document.getElementById('temp').value;

    try {
        const response = await fetch(`https://api.example.com/recommended-crops?city=${city}&area=${area}&temp=${temp}`);
        const data = await response.json();

        // Check if the API response has the expected format
        if (!data.recommendedCrops) {
            console.error('Invalid data format:', data);
            return;
        }

        const recommendedCrops = data.recommendedCrops;
        recommendedCropsList.innerHTML = '';
        recommendedCrops.forEach((crop) => {
            const listItem = document.createElement('li');
            listItem.textContent = crop.name;
            recommendedCropsList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error fetching crops:', error);
    }
});
