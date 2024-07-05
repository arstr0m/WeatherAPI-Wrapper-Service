
# Weather API Wrapper Service using Visual Crossing, Django, and Redis

This project implements a weather API wrapper service utilizing the Visual Crossing weather API, built with Django, and enhanced with Redis for efficient caching.

## Tech


<div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap;">

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)

</div>

## API Reference

#### Get Weather

```http
  GET /weather/{city_name}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `city_name` | `string` | **Returns**. JsonResponse |

### Get Redis Status
```http
  GET /test_cache
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `none` | `none` | **Returns**. REDIS CONNECTION STATUS |