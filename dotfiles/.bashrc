export GOPATH=$(go env GOPATH)
export PATH="$PATH:$GOPATH/bin"

export PS1="\[$(tput setaf 243)\]\u\[$(tput setaf 245)\]@\[$(tput setaf 249)\]\h \[$(tput setaf 254)\]\w \[$(tput sgr0)\]$ "

export EDITOR=helix

HISTCONTROL=ignoreboth:erasedups

alias goci='go vet ./... && golangci-lint run -v -j $(( $(nproc) - 1))'
alias ip='ip -c'