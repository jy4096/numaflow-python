.PHONY: image
image:
	docker build -t "quay.io/numaio/numaflow-python/async-sink-log:v0.7.0" .
# Github CI runner uses platform linux/amd64. If your local environment don't, the image built by command above might not work
# under the CI E2E test environment.
# To build an image that supports multiple platforms(linux/amd64,linux/arm64) and push to quay.io, use the following command
# docker buildx build -t "quay.io/numaio/numaflow-python/async-sink-log:latest" --platform linux/amd64,linux/arm64 . --push
# If command failed, refer to https://billglover.me/notes/build-multi-arch-docker-images/ to fix
