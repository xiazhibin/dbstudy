# coding=utf-8
'''

select * from bugs order by rand() limit 1;
问题：无法使用索引
     乱序好的顺序只要一部分，浪费。


1.选择下一个最大
select b1.* from Bugs as b1
join (select ceil(rand()* max(bug_id) from Bugs)) as bug_id) as b2
where b1.bug_id >= bug2.bug_id
order by b1.bug_id
limit 1;

'''
