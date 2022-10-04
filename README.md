Docker Hub: https://hub.docker.com/repository/docker/dogterbox/ip-info  
Git Hub: https://github.com/dogterbox/ip-info

---

Docker Run:
```bash
docker run --rm -p 8080:8080 dogterbox:ip-info
```

Response:
```json
{
    "client-ip": "x.x.x.x",
    "host-name": "xxxx",
    "host-private-ip": "x.x.x.x",
    "host-public-ip": "x.x.x.x",
    "host-request-url": "http://x.x.x.x:8080/"
}
```
