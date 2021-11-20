<template>
	<view class="root-grid-item">
		<image :src="icon" mode="aspectFit"></image>
		<text>{{title}}</text>
	</view>
</template>

<script>
	export default {
		name:'GridItem',
		props:['icon', 'title']
	}
</script>

<style>
	.root-grid-item {
		display: flex;
		justify-content: center;
		flex-wrap: wrap;
		align-items: center;
	}
	
	.root-grid-item image {
		height: 60%;
		width: 60%;
/* 		box-shadow: 5px 10px #888888; */
	}
	.root-grid-item text {
		width: 100%;
		text-align: center;
		font-weight: 500;
		font-size: 18px;
	}
</style>
