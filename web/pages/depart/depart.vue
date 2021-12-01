<template>
	<view>
		<!-- 设置背景图片 -->
		<image class="bg-set" src="../../static/backGround/科室页面背景.jpg"></image>
		<view class="grid-container">
			<view id="app">
				<Grid :items="items" :type="1" class="root-grid"></Grid>
			</view>
		</view>
	</view>
</template>

<script>
	import Grid from "../../components/Grid.vue"
	export default {
		components:{Grid},
		data() {
			return {
				items:[
					{
						icon:  require("../../static/depart/肿瘤科.png"),
						title: "肿瘤科"
					},
					{
						icon: require("../../static/depart/传染科.png"),
						title: "传染科"
					},				{
						icon:  require("../../static/depart/男科.png"),
						title: "男科"
					},					{
						icon:  require("../../static/depart/妇产科.png"),
						title: "妇产科"
					},					{
						icon:  require("../../static/depart/内科.png"),
						title: "内科"
					},					{
						icon:  require("../../static/depart/血液科.png"),
						title: "血液科"
					},					{
						icon:  require("../../static/depart/中医科.png"),
						title: "中医科"
					},					{
						icon:  require("../../static/depart/骨科.png"),
						title: "骨科"
					},					{
						icon:  require("../../static/depart/眼科.png"),
						title: "眼科"
					},					{
						icon:  require("../../static/depart/儿科.png"),
						title: "儿科"
					},					{
						icon:  require("../../static/depart/精神病科.png"),
						title: "精神病科"
					},					{
						icon:  require("../../static/depart/耳鼻喉科.png"),
						title: "耳鼻喉科"
					},					{
						icon:  require("../../static/depart/皮肤科.png"),
						title: "皮肤科"
					},					{
						icon:  require("../../static/depart/营养科.png"),
						title: "营养科"
					},					{
						icon:  require("../../static/depart/急诊科.png"),
						title: "急诊科"
					}
				]
			}
		}	
	}
</script>

<style scoped>
	.bg-set{
		position: fixed;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
		z-index: -1;
	}
	.grid-container {
		display: flex;
		align-items: center;
		justify-content: center;
		height: 670px;
	}
</style>
