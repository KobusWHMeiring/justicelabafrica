document.addEventListener('DOMContentLoaded', () => {
    
    // --- Language Modal Logic ---
    const modalOverlay = document.getElementById('language-modal-overlay');
    const langForm = document.getElementById('language-modal-form');
    
    // Check if the modal has already been shown in this session
    if (sessionStorage.getItem('languageModalShown') !== 'true') {
        
        // If not, show the modal
        if (modalOverlay) {
            modalOverlay.classList.add('modal-overlay--visible');
        }

        // Add event listeners to the language buttons
        if (langForm) {
            const langButtons = document.querySelectorAll('.language-modal__button');
            const langInput = langForm.querySelector('input[name="language"]');

            langButtons.forEach(button => {
                button.addEventListener('click', () => {
                    const langCode = button.dataset.lang;
                    if (langCode && langInput) {
                        langInput.value = langCode;
                        langForm.submit();
                    }
                });
            });
        }
        
        // Set a flag in session storage so it doesn't show again
        sessionStorage.setItem('languageModalShown', 'true');
    }

    // --- Mobile Navigation Toggle ---
    const mobileToggle = document.querySelector('.nav__mobile-toggle');
    const nav = document.querySelector('.nav');

    if (mobileToggle && nav) {
        mobileToggle.addEventListener('click', () => {
            nav.classList.toggle('nav--visible');
        });
    }

});