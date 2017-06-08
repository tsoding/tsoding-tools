lock_token() {
    echo -n "Access Token: "
    read -s TOKEN
    LOCKED_TOKEN=$(echo -n "${TOKEN}" | gpg --output - --symmetric | base64 -w0) || return 1
    echo "export ACCESS_TOKEN='${LOCKED_TOKEN}'"
}

unlock_token() {
    INTER_ACCESS_TOKEN=$(echo -n "${ACCESS_TOKEN}" | base64 -d | gpg --output - --decrypt) || return 1
    export ACCESS_TOKEN="${INTER_ACCESS_TOKEN}"
}
