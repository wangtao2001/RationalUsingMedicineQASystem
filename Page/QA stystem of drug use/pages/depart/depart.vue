<template>
	<view id="app">
		<Grid :items="items" class="root-grid"></Grid>
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

<style>
</style>
