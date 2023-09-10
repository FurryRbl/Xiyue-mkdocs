console.log("欢迎阅读茜悦 世界观 Wiki!");

// 初始化 FancyBox UI Gallery
Fancybox.bind('[data-fancybox="gallery"]', {});

// 初始化 OverlayScrollbars 滚动条
OverlayScrollbarsGlobal.OverlayScrollbars(
	document.getElementsByTagName("body")[0],
	{
		scrollbars: {
			theme: "os-theme-dark",
		},
	}
);
