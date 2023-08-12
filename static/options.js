document.addEventListener('DOMContentLoaded', function() {
  const smallImages = document.querySelectorAll('.small-image');
  smallImages.forEach(smallImage => {
    smallImage.addEventListener('mouseover', function() {
      const parentImage = this.parentNode.previousElementSibling;
      if (parentImage.nodeName === 'IMG') {
        const smallImageUrl = this.src;
        const parentImageUrl = parentImage.src;
        parentImage.src = smallImageUrl;
        this.src = parentImageUrl;
        this.classList.add('fade-in'); // add the "fade-in" class to the small image
      } else {
        console.error('Parent element is not an image!');
      }
    });
    smallImage.addEventListener("mouseout", function(){
      const parentImage = this.parentNode.previousElementSibling;
      if (parentImage.nodeName === 'IMG') {
        const smallImageUrl = this.src;
        const parentImageUrl = parentImage.src;
        parentImage.src = smallImageUrl;
        this.src = parentImageUrl;
        this.classList.remove('fade-in'); // remove the "fade-in" class from the small image
      } else {
        console.error('Parent element is not an image!');
      }      
    })
  });
});
