#! python2
# coding=utf-8

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb
my_set = db.test_set

arr = [{
	"name": "candy",
	"age": 18
},{
	"name": "lucy",
	"age": 27
}]
my_set.insert(arr)
my_set.insert({
	"name": "lily",
	"age": 19
})
# my_set.insert(arr)
