# ossm-header-routing
Simple demo to show routing based on headers via OSSM

This uses a `ServiceEntry` called `product-api-entry` in the `frontend-ns` namespace. 
  
  
The `VirtualService` named `product-api-routing` evaluates headers when the ServiceEntry is called and routes to an internal service in another namespace based on the header.   

This is for illustrative purposes, but you could use headers to route to `dev`, `test`, `prod` namespaces, for example.


## Prereq-OSSM is installed and configured

See: (OSSM3 Demo SetUp)[https://github.com/bugbiteme/ossm-3-demo]

Apply `istio.yaml` to update it to handle DNS allocation

Added config:

```yaml
  values:
    meshConfig:
      defaultConfig:
        proxyMetadata:
          ISTIO_META_DNS_AUTO_ALLOCATE: "true"
          ISTIO_META_DNS_CAPTURE: "true"
```

## Deploy Resources

```bash
oc apply -f frontend  
```

Sample output:

```bash
namespace/frontend-ns created
serviceentry.networking.istio.io/product-api-entry created
pod/curl-test created
virtualservice.networking.istio.io/product-api-routing created
```

## Test Header-Based Routing

header `hello`

```bash
oc exec -n frontend-ns curl-test -- \
  curl -s -H "x-env-target: hello" \
       http://product-api.internal/hello
```

Output:

```json
{"message":"Hello World from service-b-v2"}
```

header `dev`

```bash
oc exec -n frontend-ns curl-test -- \
  curl -s -H "x-env-target: dev" \
       http://product-api.internal/hello
```

Output:

```json
{"message":"Hello World from web-front-end"}
```

