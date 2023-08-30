async function fetchArtworks(page = randomise(), pageSize = 14) {
    const apiUrl = `https://api.artic.edu/api/v1/artworks?page=${page}&limit=${pageSize}`;
    
    try {
      const response = await fetch(apiUrl);
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error:', error);
      return null;
    }
  }

 function randomise(){
   return Math.floor((Math.random() * 10) + 1);
 } 
  
  
  async function displayArtworks() {
    const artworkListElement = document.getElementById('artworkList');
  
    try {
      const data = await fetchArtworks();
      if (data && data.data && data.data.length > 0) {
        const artworks = data.data;
        const artworksHTML = artworks.map(artwork => `
          <div class="artwork">
            <h2>${artwork.title}</h2>
            <br />
            <p>${artwork.artist_title}</p>
    
            <img src="${artwork.image_id ? `https://www.artic.edu/iiif/2/${artwork.image_id}/full/843,/0/default.jpg` : 'placeholder-image-url.jpg'}" alt="${artwork.title}">
          </div>
        `).join('');
  
        artworkListElement.innerHTML = artworksHTML;
      } else {
        artworkListElement.innerHTML = '<p>No artworks found.</p>';
      }
    } catch (error) {
      console.error('Error:', error);
      artworkListElement.innerHTML = '<p>An error occurred while fetching data.</p>';
    }
  }
  
  // Call the function to display artworks
  displayArtworks();
  
  