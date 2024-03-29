#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import gensim
import src.base
import math

stock_name = '农夫山泉'
file_name = 'a07a1b5342b75adc04ec1589b6b2d376'

seg_dir = '/segmentation/news/content/' + stock_name + '/'
save_dir = '/similarity/model/news/content/' + stock_name + '/doc2vec/vec_20_min_2_epo_20/'
data_dir = '/data/news/' + stock_name + '/'

f = open(data_dir + file_name + '.txt')
contents = f.read()
dictionary = json.loads(contents)
input_content = dictionary['content']
f.close()

#input_content = input_content[math.floor(0.1*len(input_content)):math.floor(0.8*len(input_content))]
#input_content = '中新经纬客户端1月13日电针对“疑似农夫山泉夜毁武夷山国家公园林区”的报道，12日晚间，武夷山国家公园官方微信发布通报称，经查，相关取水点不在武夷山国家公园范围内，距离公园边界有50多米；取水点附近修筑的施工便道所造成的毁林情况已由武夷山市森林公安部门在2019年11月18日立案调查。1月11日晚间，有报道称“疑似农夫山泉夜毁武夷山国家公园林区”，其中指出“疑似农夫山泉饮用水有限公司，未经国家公园管理局审批，在武夷山国家公园内使用大型器械不合规施工，破坏公园植被，影响十分恶劣。”对此，武夷山国家公园通报称，接到该网络舆情后，武夷山国家公园管理局高度重视，立即组织国家公园执法支队、森林公安分局、生态部等部门组成调查组，赶赴到现场对有关情况进行核实。网络舆情中提及的农夫山泉公司施工内容主要有以下三个地块：一是在武夷山市洋庄乡大安村大安源小组河道内拟修建一处长约30米的水坝作为取水点，目前该取水点整理了小段河道、铺设了部分水泥阻水带和四根管道。经核查，该取水点不在武夷山国家公园范围内，距离公园边界有50多米。农夫山泉公司施工地点示意图来源：武夷山国家公园官方微信二是在紧邻该取水点的林地内毁坏林木并修筑了一段长约200米的施工便道。经核查，确有修筑便道，经实地测量，长度约150米。但该处便道修筑时间为2019年10月，当时该区域并未划入武夷山国家公园范围。经福建省人民政府2019年12月25日批准的《武夷山国家公园总体规划》新调入国家公园范围。毁林情况已由武夷山市森林公安部门在2019年11月18日立案调查。三是利用大安村大安源小组原有的毛竹生产便道运输施工材料到取水点，这条原有的便道连接着农夫山泉公司新修筑的施工便道。经核查，该便道长约2公里，一直作为大安村大安源小组毛竹生产的必经之路并长期使用。根据批复的《武夷山国家公园总体规划》，该区域已调入武夷山国家公园范围。农夫山泉公司在施工时有从该便道运输建筑材料情况，但未对便道进行拓宽、整修，也未对该便道沿途的林木等周围环境损坏。农夫山泉公司开设的施工便道来源：武夷山国家公园官方微信武夷山国家公园表示，今后将进一步加大宣传力度，在深刻分析当前面临的新形势后，习近平总书记提出坚定不移推动共建“一带一路”应当落实好的“五个统筹”：统筹发展和安全、统筹国内和国际、统筹合作和斗争、统筹存量和增量、统筹整体和重点。'
#input_content = '中新经纬客户端1月13日电针对“疑似农夫山泉夜毁武夷山国家公园林区”的报道，12日晚间，武夷山国家公园官方微信发布通报称，经查，相关取水点不在武夷山国家公园范围内，距离公园边界有50多米；取水点附近修筑的施工便道所造成的毁林情况已由武夷山市森林公安部门在2019年11月18日立案调查。1月11日晚间，有报道称“疑似农夫山泉夜毁武夷山国家公园林区”，其中指出“疑似农夫山泉饮用水有限公司，未经国家公园管理局审批，在武夷山国家公园内使用大型器械不合规施工，破坏公园植被，影响十分恶劣。”对此，武夷山国家公园通报称，接到该网络舆情后，武夷山国家公园管理局高度重视，立即组织国家公园执法支队、森林公安分局、生态部等部门组成调查组，赶赴到现场对有关情况进行核实。网络舆情中提及的农夫山泉公司施工内容主要有以下三个地块：一是在武夷山市洋庄乡大安村大安源小组河道内拟修建一处长约30米的水坝作为取水点，目前该取水点整理了小段河道、铺设了部分水泥阻水带和四根管道。经核查，该取水点不在武夷山国家公园范围内，距离公园边界有50多米。农夫山泉公司施工地点示意图来源：武夷山国家公园官方微信二是在紧邻该取水点的林地内毁坏林木并修筑了一段长约200米的施工便道。经核查，确有修筑便道，经实地测量，长度约150米。但该处便道修筑时间为2019年10月，当时该区域并未划入武夷山国家公园范围。经福建省人民政府2019年12月25日批准的《武夷山国家公园总体规划》新调入国家公园范围。毁林情况已由武夷山市森林公安部门在2019年11月18日立案调查。三是利用大安村大安源小组原有的毛竹生产便道运输施工材料到取水点，这条原有的便道连接着农夫山泉公司新修筑的施工便道。经核查，该便道长约2公里，一直作为大安村大安源小组毛竹生产的必经之路并长期使用。根据批复的《武夷山国家公园总体规划》，该区域已调入武夷山国家公园范围。在深刻分析当前面临的新形势后，习近平总书记提出坚定不移推动共建“一带一路”应当落实好的“五个统筹”：统筹发展和安全、统筹国内和国际、统筹合作和斗争、统筹存量和增量、统筹整体和重点。网络文明是现代社会文明进步的重要标志。加强网络文明建设，是推进社会主义精神文明建设、提高社会文明程度的必然要求，是适应社会主要矛盾变化、满足人民对美好生活向往的迫切需要，是加快建设网络强国、全面建设社会主义现代化国家的重要任务。'
#input_content = '如今，市面上的矿泉水饮料种类繁多。相信很多人都会想到农夫山泉这个品牌。从成立之初提出的“农夫山泉，有点甜”，到现在的“我们不生产水，我们只是大自然的搬运工”。这些令人印象深刻的广告标语，让农夫山泉再一次得到了大众的广泛认可，但在成名的同时，它的商标也越来越相似。说到商标，我们先来了解一下农夫山泉的商标情况。 1996年成立后的同年，农夫山泉就在“农夫山泉有点甜”的口号之前就立即申请了“农夫山泉”商标。可见公司商标的重要性。在中国商标网搜索发现，农夫山泉有限公司共申请了与“农夫山泉”相关的商标146件，注册类别几乎涵盖了所有类型的商标。其中，最早的商标为第1139027号“农夫山泉”商标，于1996年12月23日注册，获准在23类啤酒中使用；矿泉水（饮料）；水（饮料）；茶饮料（水）；果汁等服务。近日，北京市高级人民法院就“农夫山”商标无效行政纠纷一案作出判决，驳回了上诉人农夫山（广州）乳业有限公司（以下简称“农夫山乳业公司”）的诉讼请求。 ”）。请求维持一审判决无效。 26916681号系争商标“农夫山”商标于2017年10月17日由农夫山乳业公司申请注册，获准用于29种豆奶；牛奶;豆浆等服务。今年3月5日，国家知识产权局以申请商标的中文部分主要被商标局认可为由，驳回了农夫山乳业公司的申请。 “山泉”商标的前三个字相同，整体称呼和含义没有明确区分。同时使用豆奶、乳饮料（主要是牛奶）等同类产品，极易引起相关公众的混淆和误解，已构成使用同类产品。上的类似商标。农夫山乳业公司不服，向北京知识产权法院提起行政诉讼。今年6月25日，北京知识产权法院作出一审判决，维持被诉判决。公司再次上诉至北京市高级人民法院。最终，法院认为： 1、农夫山乳业公司主张与本案基本相同的商标在第29类商品上实现共存。根据审查标准一致的原则，系争商标可以与引证商标共存。但是，每个商标的构成要素、使用的商品种类、相关公众的认知度、商业使用的状况等都存在差异。其他商标的注册与本案不同，未经司法审查不能成为争议商标。初步批准的理由。 2、农夫山乳业公司提供的证据不足以证明系争商标在长期使用后能够与引证商标进行区分。最终，26916681号“农夫山”商标经三轮审查无效。小编想说的是，除了商标的提前注册，商标检索也是避免雷同和驳回的关键步骤。专业机构可以帮您排查知识产权，做好知识产权保护工作！如果您对商标、专利、版权不了解，可以点击下方“了解更多”或私信联系易修知识产权，小编为您解答！编辑：易修知识产权'
#input_content = '现在市场上有很多种矿泉水饮料。我相信他们中的很多人都会想到农山泉的品牌。从成立之初提出的“农民的春天，有点甜”到今天的“我们不生产水，我们只是大自然的搬运工”。这些令人印象深刻的广告词使“农山泉”再次得到公众的广泛认可，但它虽然出名，但其商标却越来越相似。说到商标，我们先来了解一下农山泉的商标。1996年成立后的同一年，农山泉立即申请“农山泉”商标，比“农山泉，有点甜”的广告口号还要早。由此可见，该公司非常重视其商标。在中国商标网搜索中发现，农山弹簧有限公司已申请146个“农山弹簧”相关商标，注册类别几乎涵盖所有类型的商标。其中，最早的商标是“农山泉”商标1139027号，于1996年12月23日申请注册，批准用于23种啤酒；矿泉水（饮料）；水（饮料）；茶饮料（水）；果汁和其他服务。关于类似商标案，近日，北京市高级人民法院就“农农山”商标无效的行政纠纷作出判决，驳回上诉人农农山（广州）乳业有限公司（以下简称“农农山乳业公司”）的诉讼请求，维持一审无效判决。2017年10月17日，“农农山”商标第26916681号由农农山乳业公司申请注册，批准用于29种豆浆；牛奶豆浆和其他服务。今年3月5日，国家知识产权局驳回了农农山乳品公司的申请，理由是申请商标的中文部分与商标局引用的“农农山泉”商标第1341841号和“农农山泉”商标第25242267号的前三个字相同。整体名称和含义无明显差异，同时用于豆浆和乳饮料（主要是牛奶）等类似商品，容易引起相关公众的混淆和误解，并构成类似商品上使用的类似商标。农山乳品公司拒绝接受这一决定，随后向北京知识产权法院提起行政诉讼。今年6月25日，北京知识产权法院作出一审判决，维持被起诉的判决。该公司再次向北京市高级人民法院提起上诉。最后，法院认为：1。农山乳业公司称，与本案情况基本相同的商标已共存于29类商品中。根据审查标准的一致性原则，有争议的商标可以与被引用的商标共存。但是，每个商标的构成要素、为使用而制定的商品类别、相关公众的意识和商业使用状态不同，其他商标的注册与本案不同，且未接受司法审查，这不能成为对有争议的商标进行初步审查和批准的理由。2.农山乳业公司提供的证据不足以证明长期使用后，可将有争议的商标与引用的商标区分开来。最后，它通过了三轮考试编号26916681的“农耕山”商标仍然无效。小编想说，除了尽快注册商标外，商标查询也是避免因近似而被拒绝的关键步骤。专业的代理可以帮您检查知识产权版图，保护知识产权！如果您不了解商标、专利和版权，您可以单击下面的“了解更多信息”或通过私人信函联系益秀知识产权。小编会为你负责的！编者：益秀知识产权'
stoplists = src.base.get_stoplists()

model = gensim.models.doc2vec.Doc2Vec.load(save_dir + '/default.d2v')
input_words_list = src.base.segment_process(input_content, stoplists)

file_names_json = os.listdir(seg_dir)
inferred_vector = model.infer_vector(input_words_list)
sims = model.dv.most_similar([inferred_vector], topn=len(model.dv))
config = [('MOST', 0), ('SECOND-MOST', 1), ('MEDIAN', len(sims)//2),('LEAST', len(sims) - 1)]
outcome = list()
for label, index in config:
    output_file_name = file_names_json[sims[index][0]]
    output_f = open(data_dir + output_file_name.replace('.json','') + '.txt')
    output_contents = output_f.read()
    output_dictionary = json.loads(output_contents)
    output_content = output_dictionary['content']
    output_f.close()
    outcome.append((label,
                    sims[index][1],
                    output_file_name,
                    output_content))
print('原文：')
print(input_content)
print('\n')

for item in outcome:
    print(item)
    print('\n')
