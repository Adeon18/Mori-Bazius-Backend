extends Control


@onready var Username:  TextEdit = get_node("Username")
@onready var Password:  TextEdit = get_node("Password")
@onready var RegButton: Button = get_node("RegisterButton")
@onready var GetInfo :  Button = get_node("GetInfo")
@onready var UserId  :  TextEdit = get_node("UserId")
@onready var ResponceId:Label = get_node("ResponceId")
@onready var UserInfo:  RichTextLabel = get_node("UserInfo")

@onready var POST: HTTPRequest = get_node("POST")
@onready var GET: HTTPRequest = get_node("GET")

func _on_register_button_pressed():
	var data_to_send: Dictionary = {
		"username": Username.text,
		"password": Password.text,
	}
	var query = JSON.stringify(data_to_send)
	var url: String = "http://127.0.0.1:8000/users"
	var headers = ["Content-Type: application/json"]
	POST.request(url, headers, HTTPClient.METHOD_POST, query)

func _on_get_info_pressed():
	var url: String = "http://127.0.0.1:8000/users/" + UserId.text
	GET.request(url)


func _on_post_request_completed(result, response_code, headers, body):
#	print(response_code)
	var res = body.get_string_from_utf8()
	ResponceId.text = res
	print(res)


func _on_get_request_completed(result, response_code, headers, body):
	var res = body.get_string_from_utf8()
	UserInfo.text = res
	print(res)
