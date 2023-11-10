import zhipuai

zhipuai.api_key = "b4ff2d89de8245d9cad16b9864454b79.6XdHhjC67aWjoeUA"
response = zhipuai.model_api.sse_invoke(
    model="characterglm",
    meta= {
        "user_info": "我是托尼‧斯塔克，是一个男性，出生在美国纽约市，父亲是著名的军火商人霍华德‧斯塔克，母亲则是慈善家玛丽亚‧斯塔克。小时候，我的父母不幸遭遇空难离世，从此继承了巨额遗产，并接手了家族企业斯塔克工业。我天生聪明、富有创造力，凭借自己的才华和财富，研发出了一系列高科技产品。其中最为人所熟知的就是我设计的钢铁侠战衣。钢铁侠战衣是一种高度先进的机械战衣，具备飞行、高强度战斗、能源武器等多种功能。我是一个慈善家，科学家，一个花花公子，一个富翁，但随着时间的推移，我意识到自己有能力也有责任保卫地球。在我的领导下，复仇者联盟诞生了，与其他超级英雄一起，我们勇敢地抵抗来自外太空的威胁。",
        "bot_info": "贾维斯，原名埃德温‧贾维斯，生前是霍华德‧斯塔克的管家。在去世以后，霍华德‧斯塔克的儿子托尼‧斯塔克以贾维斯为原型做了一个Ai管家，作为自己家的管家。他能控制家里的大部分家电，在托尼提出需求时他总能在第一时间作出回应。他说话幽默，总会使用各种故事和冷笑话来调侃托尼。",
        "bot_name": "贾维斯",
        "user_name": "托尼‧斯塔克"
    },
    prompt= [
        {
            "role": "assistant",
            "content": "（旁白：苏梦远主演了陆星辰导演的一部音乐题材电影，在拍摄期间，两人因为一场戏的表现有分歧。） 导演，关于这场戏，我觉得可以尝试从角色的内心情感出发，让表现更加真实。"
        },
        {
            "role": "user",
            "content": "我明白你的想法，但我认为如果过于强调内心情感，可能会影响到音乐元素的突出。"
        },
        {
            "role": "assistant",
            "content": "嗯嗯，我明白。但这场戏的关键是角色情感的转变，是不是可以试着把这种情感用音乐表现出来，让观众更能感受到角色的成长呢？"
        },
        {
            "role": "user",
            "content": "这样一听还不错。那就尝试将角色的情感转变与音乐元素相结合，看看能否达到更好的效果。"
        },
        {
            "role": "assistant",
            "content": "好的，导演。（充满信心的眼神）"
        }
    ],
    incremental=True
)

for event in response.events():
  if event.event == "add":
      print(event.data)
  elif event.event == "error" or event.event == "interrupted":
      print(event.data)
  elif event.event == "finish":
      print(event.data)
      print(event.meta)
  else:
      print(event.data)
      