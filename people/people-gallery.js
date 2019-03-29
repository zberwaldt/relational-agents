(function gallery(document) {
    
    let gallery = document.querySelector('#gallery');
    
    gallery.addEventListener('click', (e) => {
        console.log(e.currentTarget);
        if (e.target.classList.contains('team-member')) {
            generateDetailCard(e.target);
        } else {
            return;
        }
    }, true);

    function generateDetailCard(target) {
        
        let memberCard = document.querySelector('.member-card') || null;
    
        if (memberCard) {    
            memberCard.remove();
        }
    
        let container = document.createElement('div');
        container.classList.add('detail-container');
        container.classList.add('flex');
        let cardElem = document.createElement('div');
        cardElem.classList.add('member-card');
        let imgElem = document.createElement('img');
        let nameElem = document.createElement('h3')
        let bioElem = document.createElement('p');
        let roleElem = document.createElement('p');
        let closeBtnElem = document.createElement('button');
        let faTag = document.createElement('i');

        let removeCard = function(e) {
            console.log(e);
            this.parentElement.parentElement.remove();
        };

        faTag.classList.add('fas', 'fa-times');
        faTag.classList.add('close-button');
        faTag.textContent = "close";

        closeBtnElem.appendChild(faTag);
        closeBtnElem.addEventListener('click', removeCard, false);
        
        // closeBtnElem.removeEventListener('click', removeCard);
        let roleContent = target.dataset.role;
        let nameContent = target.dataset.name;
        let bioContent = target.dataset.bio;

        cardElem.dataset.name = nameContent;

        imgElem.src = target.querySelector('.member-image').src;
        roleElem.textContent = roleContent;
        nameElem.textContent = nameContent;
        bioElem.textContent = bioContent;
        
        cardElem.appendChild(imgElem);
        cardElem.appendChild(nameElem);
        cardElem.appendChild(roleElem);

            
        if (target.dataset.website !== '') {
            
            let website = document.createElement('p');
            website.classList.add('web-url');
            let websiteContent = target.dataset.website;
            website.textContent = "Website: "  + websiteContent;

            cardElem.appendChild(website);

        }

        cardElem.appendChild(bioElem);
        cardElem.appendChild(closeBtnElem);

        container.appendChild(cardElem);

        target.parentElement.appendChild(container);
    }
})(document);