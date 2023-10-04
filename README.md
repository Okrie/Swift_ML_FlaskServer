# Swift_ML_FlaskServer
 Python Flask로 Swift로 제작한 스팀 게임 추천 어플리케이션에서 요청하는 서버 제작    
프로젝트 내 필요한 부분 API로 제작

            
<a href="https://drive.google.com/file/d/1qHqKLu0GyGhnnWPXxShAt8p64OAyyo5H/view?usp=sharing">![cover](https://github.com/Okrie/Swift_ML_FlaskServer/assets/24921229/174c1db5-4a06-4e8b-a2db-69800697e92d)</a>     

---

## 기능 설명
    
- 현재 유저의 정상적인 Login 기능이 아닌 유저 id로 정보를 확인하여 공개 설정된 내용만 노출
- 추후 Steam Login 기능을 추가할 예정    
    
**USER**
- /user/?userid={NICKNAME : STRING}    
    user의 Nickname을 검색해 steamid를 찾는 용도로 사용
- /user/getuser?steamid={STEAMD64ID : INTEGER}    
    user의 SteamId로 유저 상세 정보를 확인  
- /user/getuserfriends?steamid={STEAMD64ID : INTEGER}    
    user의 친구 목록을 불러온다
- /user/getuserdetails?steamid={STEAMD64ID : INTEGER}    
    user의 보유중인 게임을 전부 불러온다

**GAME**
- /game/searchgames?search={GAME_NAME : STRING}    
    게임을 검색할때 사용하여 게임 이름을 텍스트로 받아 상세 정보를 가져옴
- /game/searchgamesid?searchid={APPID : INTEGER}    
    게임을 검색할때 사용하며 appid를 사용하여 상세정보를 가져옴
- /game/bestgame    
    STEAM 메인 페이지 내 추천 리스트 10개를 받아와 appid를 가져옴



**LOGIN**
- /user/login?userid={NICKNAME:String}    
    현재 정상적인 기능이 아니며 유저 닉네임으로 간이 로그인 한 것처럼 노출    
    App 에서 유저가 로그인 시 게임 추천 머신러닝 후 결과를 리턴    
    

---
    
#### 기술 스택
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=git,github,vscode,python" />
  </a>
    <img src="https://cdn.icon-icons.com/icons2/70/PNG/512/ubuntu_14143.png" height="53" title="Ubuntu">
    <img src="https://cdn.icon-icons.com/icons2/512/PNG/512/prog-flask_icon-icons.com_50797.png" height="53" title="Flask">
    <img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/slack_tile_logo_icon_168820.png" height="53" title="Slack">
    <img src="https://cdn.icon-icons.com/icons2/836/PNG/512/Trello_icon-icons.com_66775.png" height="53" title="Trello">
    <img src="https://cdn.icon-icons.com/icons2/3221/PNG/512/docs_editor_suite_docs_google_icon_196688.png" height="53" title="Google Docs"> 
</p>
    
---
---
    

## 기능 상세 설명

**User**

---
- user 검색

```python
/user/?userid={NICKNAME : STRING}
```

#### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| userid  |   String | Require |

#### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | ![image](https://github.com/Okrie/Swift_ML_FlaskServer/assets/24921229/48fdebd5-a651-48d7-89c8-9ce4531cd5d7) |

- user 상세 정보

```python
/user/getuser?steamid={STEAMD64ID : INTEGER}
```

#### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| steamid  |   INTEGER | Require |

#### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | ![image](https://github.com/Okrie/Swift_ML_FlaskServer/assets/24921229/48fdebd5-a651-48d7-89c8-9ce4531cd5d7) |


- user 친구 목록

```python
/user/getuserfriends?steamid={STEAMD64ID : INTEGER}
```

#### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| steamid  |   INTEGER | Require |

#### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | ![image](https://github.com/Okrie/Swift_ML_FlaskServer/assets/24921229/53e94a8a-abcf-41d7-8882-67e09e17b042) |


- user 보유 중인 game list

```python
/user/getusergames?steamid={STEAMD64ID : INTEGER}
```

#### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| steamid  |   INTEGER | Require |

#### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | ![image](https://github.com/Okrie/Swift_ML_FlaskServer/assets/24921229/1409d891-8b39-439f-86a8-6e4e9c87b6ad) |

- user 프로필 img, level, badges

```python
/user/getuserdetails?steamid={STEAMD64ID : INTEGER}
```

#### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| steamid  |   INTEGER | Require |

#### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | ![image](https://github.com/Okrie/Swift_ML_FlaskServer/assets/24921229/84b4d5eb-9eab-4f11-a53e-8eaeb76aa0c2) |



**GAME**

---
    
- game 검색 : STRING

```python
/game/searchgames?search={GAME_NAME : STRING}
```

#### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| steamid  |   INTEGER | Require |

#### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | ![image](https://github.com/Okrie/Swift_ML_FlaskServer/assets/24921229/606ceaac-6890-48d1-ad1b-ec47cd96ad76) |
    
- game 검색 : APPID

```python
/game/searchgamesid?searchid={APPID : INTEGER}
```

#### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| steamid  |   INTEGER | Require |

#### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | ![image](https://github.com/Okrie/Swift_ML_FlaskServer/assets/24921229/9353403d-c1ba-4c7b-91a1-250033964cd5) |

- Top 10 Game : NO_PARAMETER

```python
/game/bestgame
```

#### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| count  |   INTEGER | Option |

#### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | ![image](https://github.com/Okrie/Swift_ML_FlaskServer/assets/24921229/9d4ef642-61a4-4cd6-9641-3b8cf6c03a43) |


**LOGIN**

---
- App 에서 유저가 로그인 시 게임 추천 머신러닝 후 결과를 리턴

```python
/user/login?userid={NICKNAME:STRING}
```

#### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| userid  |   String | Required |

#### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | ![image](https://github.com/Okrie/Swift_ML_FlaskServer/assets/24921229/07c26371-5cb4-4cd5-be39-e3d4292d2831) |
