export default {
    container_id: "viz",
    server_url: "neo4j://localhost:7687",
    server_user: "neo4j",
    server_password: "qazplm-55454",
	labels: {  // 图谱渲染配置文件
		"辨证法": {
			"caption": "辨证法名称",
			"size": "point",
			"title_properties": [
				"辨证法名称",
				"辨证法含义"
			]
		},
		"证候分类": {
			"caption": "证候分类名称",
			"size": "point",
			"title_properties": [
				"证候分类名称",
				"证候分类英文名",
				"证候分类含义"
			]
		},
		"证候":{
			"caption": "证候名称",
			"size": "point",
			"title_properties": [
				"证候名称",
				"证候英文名",
				"临床表现",
				"证候病机"
			]
		},
		"美容方剂": {
			"caption": "方剂名",
			"size": "point",
			"title_properties": [
				"方剂名",
				"配伍用量",
				"功效",
				"用法",
				"来源",
				"治法",
				"备注"
			]
		},
		"皮肤病": {
			"caption": "皮肤病名称",
			"size": "point",
			"title_properties": [
				"皮肤病名称",
				"皮肤病症状特点",
				"皮肤病病因病理",
				"皮肤病定义"
			]
		},
		"方剂分类": {
			"caption": "方剂分类名称",
			"size": "point",
			"title_properties": [
				"方剂分类名称"
			]
		},
		"方剂": {
			"caption": "方剂名称",
			"size": "point",
			"title_properties": [
				"方剂名称",
				"功效主治",
				"药材配方",
				"方剂用法",
				"方剂出处"
			]
		},
		"其他治法": {
			"caption": "其他治法名",
			"size": "point",
			"title_properties": [
				"其他治法名",
				"具体治法"
			]
		},
		"中药分类":{
			"caption": "中药分类名称",
			"size": "point",
			"title_properties": [
				"中药分类名称"
			]
		},
		"中药": {
			"caption": "中药名称",
			"size": "point",
			"title_properties": [
				"中药名称",
				"中药别名",
				"中药出处",
				"功效主治",
				"中药种属",
				"性味归经",
				"形态特征",
				"功能主治",
				"保存方法",
			],
		},
		"symptom": {
			"caption": "name",
			"size": "point",
			"title_properties": [
				"name",
				"describe",
				"cause",
				"interrogation"
			]
		},
		"medical": {
			"caption": "name",
			"size": "point",
			"title_properties": [
				"name",
				"product_name",
				"en_name",
				"ingredient",
				"character",
				"disease",
				"function",
				"usage",
				"adverse_reaction",
				"taboo",
				"attention",
				"depot",
				"size",
				"package_size",
				"date",
				"number",
				"company"
			]
		},
		"disease": {
			"caption": "name",
			"size": "point",
			"title_properties": [
				"name",
				"another_name",
				"people",
				"site",
				"cure_rate",
				"description"
			]
		},
		"department": {
			"caption": "name",
			"size": "point",
			"title_properties": [
				"name"
			]
		},
		"check": {
			"caption": "name",
			"size": "point",
			"title_properties": [
				"name",
				"describe",
				"site",
				"is_fasting",
				"taboo",
				"price",
				"indicator",
				"atten",
				"purpose",
				"process"
			]
		}
	}
}