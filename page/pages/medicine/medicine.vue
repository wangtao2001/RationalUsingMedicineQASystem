<template>
	<view>
		<image class="bg-set" src="../../static/backGround/中药页面背景.jpg"></image>
		<view class="grid-container">
			<view id="app">
				<Grid :items="items" :type="3" class="root-grid"></Grid>
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
						icon:  require("../../static/medicine/安神药.png"),
						title: "安神药"
					},
					{
						icon:require("../../static/medicine/拔毒生肌药.png"),
						title:"拔毒生肌药"
					},
					{
						icon:  require("../../static/medicine/补虚药.png"),
						title: "补虚药"
					},
					{
						icon:  require("../../static/medicine/芳香化湿药.png"),
						title: "芳香化湿药"
					},
					{
						icon:  require("../../static/medicine/活血化瘀药.png"),
						title: "活血化瘀药"
					},
					{
						icon:  require("../../static/medicine/解表药.png"),
						title: "解表药"
					},
					{
						icon:  require("../../static/medicine/解毒杀虫药.png"),
						title: "解毒杀虫药"
					},
					{
						icon:  require("../../static/medicine/开窍药.png"),
						title: "开窍药"
					},
					{
						icon:  require("../../static/medicine/理气药.png"),
						title: "理气药"
					},
					{
						icon:  require("../../static/medicine/利水渗湿药.png"),
						title: "利水渗湿药"
					},
					{
						icon:  require("../../static/medicine/平喘药.png"),
						title: "平喘药"
					},
					{
						icon:  require("../../static/medicine/平肝息风药.png"),
						title: "平肝熄风药"
					},
					{
						icon:  require("../../static/medicine/清热药.png"),
						title: "清热药"
					},
					{
						icon:  require("../../static/medicine/驱虫药.png"),
						title: "驱虫药"
					},
					{
						icon:  require("../../static/medicine/祛风湿药.png"),
						title: "祛风湿药"
					},
					{
						icon:  require("../../static/medicine/收涩药.png"),
						title: "收涩药"
					},
					{
						icon:  require("../../static/medicine/温里药.png"),
						title: "温里药"
					},
					{
						icon:  require("../../static/medicine/消食药.png"),
						title: "消食药"
					},
					{
						icon:  require("../../static/medicine/泻下药.png"),
						title: "泻下药"
					},
					{
						icon:  require("../../static/medicine/涌吐药.png"),
						title: "涌吐药"
					},
					{
						icon:  require("../../static/medicine/燥湿止痒药.png"),
						title: "燥湿止痒药"
					},
					{
						icon:  require("../../static/medicine/止咳化痰药.png"),
						title: "止咳化痰药"
					},
					{
						icon:  require("../../static/medicine/止血药.png"),
						title: "止血药"
					},
					{
						icon:  require("../../static/medicine/其他中草药.png"),
						title: "其他中草药"
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
	.root-grid{
		height: 360px;
		width: 1000px;
	}
	.grid-container {
		display: flex;
		align-items: center;
		justify-content: center;
		height: 670px;
	}
</style>

