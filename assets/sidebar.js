// setTimeout(() => {
window.onload = () => {

	console.log("Entré")
	setTimeout(() => {
		const sidebarBox = document.querySelector('.sidebar-wrapper'),
		sidebarBtn = document.querySelector('.btn'),
			contentWrapper = document.querySelector('.content');
			sidebarBtn.addEventListener('click', event => {
		console.log('Presionado')
		sidebarBtn.classList.toggle('active');
		sidebarBox.classList.toggle('active');
		});
		contentWrapper.addEventListener('click', event => {
				
			if (sidebarBox.classList.contains('active')) {
					
				sidebarBtn.classList.remove('active');
				sidebarBox.classList.remove('active');
			}
		});

		window.addEventListener('keydown', event => {

			if (sidebarBox.classList.contains('active') && event.keyCode === 27) {
				sidebarBtn.classList.remove('active');
				sidebarBox.classList.remove('active');
			}
		})
	},2000)
	
}
// 	}, 100
// )