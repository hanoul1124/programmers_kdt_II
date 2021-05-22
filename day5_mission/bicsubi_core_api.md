# 빅수비 코어 API

API 명세



### 1. `GET /whoami`

- github id를 반환한다.

- ```json
    {
        "name" : "hanoul1124"
    }
    ```



### 2. `GET /echo?string="string"`

- Query String : `string`

- `string`을 반환한다.

- ```json
    {
       "value" : "string"
    }
    ```



### 3. weapon API

### 3-1. `GET /weapon`

- 무기 목록을 모두 반환한다.

- ```json
    [
        {
            "id": 2,
            "name": "Gun",
            "stock": 10
        },
        {
            "id": 3,
            "name": "Axe",
            "stock": 33
        }
    ]
    ```



### 3-2. `POST /weapon`

- 다음과 같은 JSON request에 따라 새로운 무기를 DB에 저장하고, 이를 리턴한다.

- id는 자동으로 증가하며 등록된다(Auto Increment). 따라서 이를 제외한 항목만을 전달한다.

- ```json
    {
    	"name": "test_weapon",
    	"stock": 12
    }
    ```

- DB에 새로운 아이템을 저장한 후, 다음과 같은 응답을 반환한다.

- ```json
    {
            "id": 4,
            "name": "test_weapon",
            "stock": 12
     }
    ```



### 3-3. `DELETE /weapon/<int:id>`

- id를 URI 인자로 request를 요청한다.

- 해당 id와 일치하는 아이템을 DB에서 찾아,

    - 일치하는 경우, 아이템을 삭제한 후 다음과 같은 메세지를 보낸다.

    - ```json
        {"message": f"Weapon ID:{id}가 성공적으로 삭제되었습니다."}
        ```

    - 일치하는 아이템이 없는 경우, 다음과 같은 메세지를 보낸다.

    - ```json
        {"message": "전달된 ID에 해당하는 Weapon이 존재하지 않습니다."}
        ```

    

### 3-4. `PUT /weapon/<int:id>`

- 다음과 같은 JSON request에 따라 기존 아이템의 값을 수정하고, 이를 리턴한다.

- ```json
    {
    	"name": "updated_weapon",
    	"stock": 999
    }
    ```

- id를 URI 인자로 request를 요청한다.

- 해당 id와 일치하는 아이템을 DB에서 찾아,

    - 일치하는 경우, 아이템을 request에서 전달한 JSON 값으로 업데이트 한 후 다음과 같은 메세지를 보낸다.

    - ```json
        {
                "id": 4,
                "name": "updated_weapon",
                "stock": 999
         }
        ```

    - 일치하는 아이템이 없는 경우, 다음과 같은 메세지를 보낸다.

    - ```json
        {"message": "전달된 ID에 해당하는 Weapon이 존재하지 않습니다."}
        ```

