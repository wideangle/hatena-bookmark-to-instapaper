#!/opt/local/bin/perl

#
# HatenaBookmark -> Instapaper
# Takashi Kiuchi (id:wideangle)
#

use utf8;
use strict;
use warnings;

use CGI qw/-utf8 :standard/;
use WWW::Instapaper::Client;

# はてなブックマーク Web Hook から URL を取得する

my $req = CGI->new();

if ($req->param('key') ne 'hogefuga') {
    # API Key が一致しなかった場合エラー終了
    die "Authentication failed";
}

my $url     = $req->param('url');
my $title   = $req->param('title');
my $comment = $req->param('comment');
my $status  = $req->param('status');


# Instapaper に投げる (WWW::Instapaper::Client)

if ($status ne 'add') {
    # ブックマーク追加以外の場合は何もせずに終了する。
    exit 1;
}

my $paper = WWW::Instapaper::Client->new(
    username => 'hoge@fuga.com', # E-mail OR username
    password => 'fugahoge',
    );

my $result = $paper->add (
    url       => $url,
    title     => $title,        # はてブから取得した記事タイトルを使用
    selection => $comment,      # ブックマークのコメントを追加
    );

if (defined $result) {
    print "URL added: ", $result->[0], "\n"; # http://instapaper.com/go/######
    print "Title: ", $result->[1], "\n";     # Title of page added
} else {
    warn "Was error: " . $paper->error . "\n";
}

exit 0;
