const form = document.getElementById('crop-form');
const recommendedCropsList = document.getElementById('recommended-crops');

form.addEventListener('submit', (e) => {
   e.preventDefault();
   const city = document.getElementById('city').value;
   const area = document.getElementById('area').value;
   const temp = document.getElementById('temp').value;

   // Call API to get recommended crops based on input values
   fetch(`https://api.example.com/recommended-crops?city=${city}&area=${area}&temp=${temp}`)
       .then(response => response.json())
       .then(data => {
           const recommendedCrops = data.recommendedCrops;
           recommendedCropsList.innerHTML = '';
           recommendedCrops.forEach((crop) => {
               const listItem = document.createElement('li');
               listItem.textContent = crop.name;
               recommendedCropsList.appendChild(listItem);
           });
       })
       .catch(error => console.error(error));
});
