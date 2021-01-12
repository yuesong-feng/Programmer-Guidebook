在父组件使用子组件的代码中，为子组件加上`ref="name(自己设置一个名称)"`
然后在代码中：
```javascript
this.$refs.name(你设置的名字).data	//获取子组件data中的数据
this.$refs.name(你设置的名字).method()	//获取子组件中method中的方法
```
!!!注意：如果父组件以循环的方式生成子组件，如：

```javascript
<component ref="getParameters"
           		  v-for="(item, index) in layers"
                  :is="item.name"
                  :key="index"
              ></component>
```
则`this.$refs.name(你设置的名字)`将会是一个VueComponent数组，这时候可以先获取数组的长度，再依次遍历：

```javascript
for(let i=0; i<this.$refs.name(你设置的名字).length; i++){
	this.$refs[i].name(你设置的名字).method()
	console.log(this.$refs[i].name(你设置的名字).data)
}
```
例子：
父组件代码：

```javascript
<template>
  <div>
  	<my_component ref="child_component"></my_component>
  </div>
</template>

<script>
import child_component from "./child_component"
export default {
  data: () => ({}),
  components:{
        'my_component':child_component
    },
  methods:{
  	get_data_from_child_component(){
  		this.$refs.child_component.whatever()	//父组件调用子组件的方法
  		console.log(this.$refs.child_component.msg)	//父组件调用子组件的值
  	}
  },
  mounted(){
  	this.get_data_from_child_component()
  },
};
</script>
```

子组件代码：

```javascript
<template>
  <div></div>
</template>

<script>
export default {
  data: () => ({
  	msg:"这是子组件的值",
  }),
  methods:{
  	whatever(){
  		alert("这是子组件的方法")
  	}
  }
};
</script>

```

