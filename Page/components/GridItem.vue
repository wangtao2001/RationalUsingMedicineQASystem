<template>
	<view class="root-grid-item" @click="navigateToDetails">
		<image :src="icon" mode="aspectFit"></image>
		<text>{{title}}</text>
	</view>
</template>

<script>
	export default {
		name:'GridItem',
		props:['icon', 'title'],
		methods:{
			navigateToDetails() {
				uni.navigateTo({
					// 坑，要写调用组件页面的相对路径
					url: `../../pages/details/details?title=${this.title}&type=1`, 
					success: () => {console.log('跳转成功')},
					fail: () => {console.log('跳转失败')}
				})
			}
		}
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
	}
	.root-grid-item text {
		width: 100%;
		text-align: center;
		font-weight: 500;
		font-size: 18px;
	}
</style>
