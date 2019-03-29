(function(document) {
    document.addEventListener('DOMContentLoaded', (e) => {
        console.log("loaded");
        const nextBtn = document.getElementById('next-item');
        const prevBtn = document.getElementById('prev-item');
        const newsItems = document.querySelectorAll('.news-item');
        let currentNews = 0;
        let timeoutID;
        let newsCycleID = startNewsCycle(currentNews);

        nextBtn.addEventListener('click', (e) => {
            clearInterval(newsCycleID);
            if (timeoutID != null) {
                clearTimeout(timeoutID);
            }
            if (currentNews < (newsItems.length - 1)) {
                currentNews++;
            } else {
                currentNews = 0;
            }   
            cycleItems(newsItems, currentNews);
            timeoutID = setTimeout(() => {
                newsCycleID = startNewsCycle(currentNews);
            }, 2000);
        });

        prevBtn.addEventListener('click', (e) => {
            if (timeoutID != null) {
                clearTimeout(timeoutID);
            }
            clearInterval(newsCycleID);
            if (currentNews > 0) {
                currentNews--;
            } else {
                currentNews = (newsItems.length - 1);
            }
            cycleItems(newsItems, currentNews);
            timeoutID = setTimeout(() => {
                newsCycleID = startNewsCycle(currentNews);
            }, 2000);
        });

        function startNewsCycle(currentItem) {
            return setInterval(function() {
                cycleItems(newsItems, currentItem);
                // if the currentNews index is less than the length...
                if(currentItem < newsItems.length - 1) {
                    currentItem++; // increment the currentNews index
                } else {
                    currentItem = 0; // reset the currentNews index
                }
            }, 3000);
        }

        function cycleItems(elemList, nextItem) {
            for(let i = 0; i < elemList.length; i++) {
                if (i == nextItem) {
                    elemList[i].classList.add('active');
                } else {
                    elemList[i].classList.remove('active');
                }
            }
        }

    });
    
})(document);