<template>
	<view class="root-grid">
		<grid-item class="grid-item" v-for="item in items" :icon="item.icon" :title="item.title"></grid-item>
	</view>
</template>

<script>
	import GridItem from "./GridItem.vue"
	export default {
		name:'Grid',
		components:{GridItem},
		props:["items"]
	}
</script>

<style>
	.root-grid {
		display: flex;
		justify-content: center;
		flex-wrap: wrap;;
	}
	
	.grid-item {
		width: 20%;
		height: 33.3%;
	}

</style>
