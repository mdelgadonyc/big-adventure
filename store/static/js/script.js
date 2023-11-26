function getCSRFToken() {
    var csrfCookie = document.cookie.match(/csrftoken=([^ ;]+)/)
    return csrfCookie ?csrfCookie[1] : null;
}

document.addEventListener('DOMContentLoaded', () => {

    const cartCountElement = document.getElementById('cart-count');
    const addToCartBtn = document.getElementById('addToCartBtn');

    addToCartBtn.addEventListener('click', () => {
        let currentCount = parseInt(cartCountElement.textContent) || 0;
        currentCount++;

        const url = 'update-cart-count';

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
//            body: JSON.stringify({ currentCount })
        })
            .then(response => response.json())
            .then(json => console.log("text fetched: ", json))
            .catch(error => console.error(error));

        cartCountElement.textContent = currentCount;
        console.log(currentCount);
    });
});
