document.addEventListener('DOMContentLoaded', () => {
    const reelsContainer = document.querySelector('.slide-reel');
    const loader = document.getElementById('loader');
    const videoModal = document.getElementById('video-modal');
    const modalVideo = document.getElementById('modal-video');
    const closeModal = document.getElementById('close-modal');
    const prevReelBtn = document.getElementById('prev-reel');
    const nextReelBtn = document.getElementById('next-reel');
    const shareButton = document.getElementById('share-button');
    let page = 2; // Load from page 2 onward since page 1 is pre-loaded
    let isLoading = false;
    let currentReelIndex = null;
    let allReels = [];

    // Function to open modal and play video
    const openModal = (reelIndex) => {
        const reel = allReels[reelIndex];
        if (reel) {
            modalVideo.src = reel.video_url;
            videoModal.classList.add('active');
            modalVideo.play();
            currentReelIndex = reelIndex;
        }
    };

    // Function to close modal and reset video
    const closeVideoModal = () => {
        modalVideo.pause();
        modalVideo.currentTime = 0;
        modalVideo.src = '';
        videoModal.classList.remove('active');
        currentReelIndex = null;
    };

    // Close modal button
    closeModal.addEventListener('click', closeVideoModal);

    // Share button logic
    shareButton.addEventListener('click', () => {
        if (currentReelIndex !== null) {
            const reel = allReels[currentReelIndex];
            if (reel) {
                const shareData = {
                    title: reel.title || 'Check out this video!',
                    text: 'Check out this video from The Champions Club!',
                    url: `${window.location.origin}/reels/${reel.id}`,  // Generate a proper share URL
                };

                if (navigator.share) {
                    navigator.share(shareData)
                        .then(() => console.log('Shared successfully!'))
                        .catch((error) => console.error('Share failed:', error));
                } else {
                    // Fallback: Copy URL to clipboard
                    navigator.clipboard.writeText(shareData.url)
                        .then(() => alert('Link copied to clipboard!'))
                        .catch((error) => console.error('Could not copy text: ', error));
                }
            }
        }
    });

    // Close modal if clicked outside of the video content
    videoModal.addEventListener('click', (event) => {
        if (event.target === videoModal) {
            closeVideoModal();
        }
    });

    // Event delegation to handle click on dynamically loaded reels
    reelsContainer.addEventListener('click', (event) => {
        const reelElement = event.target.closest('.reel');
        if (reelElement) {
            const reelIndex = parseInt(reelElement.getAttribute('data-reel-index'), 10);
            if (!isNaN(reelIndex)) {
                openModal(reelIndex);
            }
        }
    });

    // Previous and Next Reel Buttons
    prevReelBtn.addEventListener('click', () => {
        if (currentReelIndex > 0) {
            openModal(currentReelIndex - 1);
        }
    });

    nextReelBtn.addEventListener('click', () => {
        if (currentReelIndex < allReels.length - 1) {
            openModal(currentReelIndex + 1);
        } else {
            // Load more reels if available
            loadMoreReels().then(() => {
                if (currentReelIndex < allReels.length - 1) {
                    openModal(currentReelIndex + 1);
                }
            });
        }
    });

    // Load more reels function
    const loadMoreReels = () => {
        isLoading = true;
        loader.style.display = 'block';
        return fetch(`${loadMoreUrl}?page=${page}`)
            .then(response => response.json())
            .then(data => {
                const newReels = data.reels;
                if (newReels.length > 0) {
                    newReels.forEach((reelData) => {
                        const reelIndex = allReels.length;
                        allReels.push(reelData);

                        const reelDiv = document.createElement('article');
                        reelDiv.classList.add('reel');
                        reelDiv.setAttribute('data-video-url', reelData.video_url);
                        reelDiv.setAttribute('data-reel-index', reelIndex);

                        const thumbnailDiv = document.createElement('div');
                        thumbnailDiv.classList.add('thumbnail');

                        const img = document.createElement('img');
                        img.src = reelData.thumbnail_url || '/static/images/default-thumbnail.jpg';
                        img.alt = reelData.title;
                        thumbnailDiv.appendChild(img);

                        const overlayDiv = document.createElement('div');
                        overlayDiv.classList.add('overlay');

                        const playButtonDiv = document.createElement('div');
                        playButtonDiv.classList.add('play-button');
                        playButtonDiv.innerHTML = '<i class="fas fa-play-circle"></i>';

                        overlayDiv.appendChild(playButtonDiv);
                        thumbnailDiv.appendChild(overlayDiv);

                        reelDiv.appendChild(thumbnailDiv);

                        // Append the new reel to the reels container
                        reelsContainer.appendChild(reelDiv);
                    });
                    page += 1;
                    isLoading = false;
                    loader.style.display = 'none';
                } else {
                    loader.textContent = '';
                    infiniteObserver.unobserve(loader);
                }
            })
            .catch(error => {
                console.error('Error loading more reels:', error);
                loader.textContent = 'Error loading reels.';
            });
    };

    // Initialize existing reels on page load
    const initializeReels = () => {
        const reelElements = document.querySelectorAll('.reel');
        reelElements.forEach((reelElement, index) => {
            const videoUrl = reelElement.getAttribute('data-video-url');
            const thumbnailUrl = reelElement.querySelector('img').src;
            const title = reelElement.querySelector('img').alt;
            const id = reelElement.getAttribute('data-reel-id');

            const reelData = {
                video_url: videoUrl,
                thumbnail_url: thumbnailUrl,
                title: title,
                id: id,
            };

            allReels.push(reelData);
            reelElement.setAttribute('data-reel-index', index);
        });
    };

    initializeReels();

    // Infinite scroll to load more reels when reaching the bottom of the page
    const infiniteObserver = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting && !isLoading) {
            loadMoreReels();
        }
    }, {
        root: null,
        rootMargin: '0px',
        threshold: 1.0
    });

    infiniteObserver.observe(loader);
});
