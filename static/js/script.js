// Add smooth scrolling to all links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 70,
                behavior: 'smooth'
            });
        }
    });
});

// Add animation to product cards when they come into view
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = 1;
            entry.target.style.transform = 'translateY(0)';
            entry.target.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        }
    });
}, observerOptions);

document.querySelectorAll('.product-card, .highlight-card').forEach(card => {
    card.style.opacity = 0;
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(card);
});

// Add hover animations to product cards
document.querySelectorAll('.product-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px) scale(1.02)';
        this.style.boxShadow = '0 15px 30px rgba(0, 0, 0, 0.2)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
        this.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.1)';
    });
});

// Add hover animations to highlight cards
document.querySelectorAll('.highlight-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px) scale(1.02)';
        this.style.boxShadow = '0 15px 30px rgba(0, 0, 0, 0.2)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
        this.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.1)';
    });
});

// Add fade-in animation to hero section on page load
window.addEventListener('load', function() {
    const hero = document.querySelector('.hero');
    hero.style.opacity = '0';
    hero.style.transform = 'translateY(-20px)';
    
    setTimeout(() => {
        hero.style.transition = 'opacity 1s ease, transform 1s ease';
        hero.style.opacity = '1';
        hero.style.transform = 'translateY(0)';
    }, 100);
});

// Add pulsing animation to the top product banner
const topProductBanner = document.querySelector('.card.border-0.shadow-lg');
if (topProductBanner) {
    setInterval(() => {
        topProductBanner.style.transform = 'scale(1.01)';
        setTimeout(() => {
            topProductBanner.style.transform = 'scale(1)';
        }, 500);
    }, 3000);
}

// Add floating animation to the logo in navbar
const logo = document.querySelector('.navbar-brand img');
if (logo) {
    setInterval(() => {
        logo.style.transform = 'translateY(-3px)';
        setTimeout(() => {
            logo.style.transform = 'translateY(0)';
        }, 500);
    }, 2000);
}

// Filter products by category
function filterProducts(category) {
    // Remove active class from all links
    document.querySelectorAll('.category-link').forEach(link => {
        link.classList.remove('active');
    });
    
    // Add active class to clicked link
    event.target.classList.add('active');
    
    // Show all products if 'All Products' is clicked
    if (category === 'all') {
        document.querySelectorAll('.product-item').forEach(item => {
            item.style.display = 'block';
        });
    } else {
        // Show only products matching category
        document.querySelectorAll('.product-item').forEach(item => {
            const itemCategory = item.getAttribute('data-category');
            if (itemCategory === category) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }
}