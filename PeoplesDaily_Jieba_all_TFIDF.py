



<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>Computational-Journalism-for-People-s-Daily-Opinion/PeoplesDaily_Jieba_all_TFIDF.py at master · puconghan/Computational-Journalism-for-People-s-Daily-Opinion</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="puconghan/Computational-Journalism-for-People-s-Daily-Opinion" name="twitter:title" /><meta content="Computational-Journalism-for-People-s-Daily-Opinion - Statistical topic models – one of the sub fields of machine learning and natural language processing – provide a data-driven framework for ana" name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/1655602?v=3&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/1655602?v=3&amp;s=400" property="og:image" /><meta content="puconghan/Computational-Journalism-for-People-s-Daily-Opinion" property="og:title" /><meta content="https://github.com/puconghan/Computational-Journalism-for-People-s-Daily-Opinion" property="og:url" /><meta content="Computational-Journalism-for-People-s-Daily-Opinion - Statistical topic models – one of the sub fields of machine learning and natural language processing – provide a data-driven framework for analyzing collections of text documents. It has become one of the most frequently used tools for computational journalism used to investigate abstract topics and keywords that occur in a collection of text documents. Digital journalists can use such tools to extract frequently appearing terms, and to analyze the trend of a particular news brand or stories about a social event. Articles, analyses and documents written in Chinese have become increasingly important for multimedia stories about China. Available Chinese archives on the Internet might contain stories that require digital journalists to apply appropriate topic modeling tools. Unlike English and other alphabetic languages, the basic structural unit of Chinese language is character encoded in Guobiao GB18030 or Unicode.  I implement apps using the Chinese topic-modeling tools jieba for computational journalism. This app analyzes articles from the opinion archive of the People’s Daily and generate a list of frequently appearing words using the keyword extraction tool provided by the jieba library." property="og:description" />

      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="6AB92782:2FD3:345CB9C:549929B7" name="octolytics-dimension-request_id" /><meta content="6202843" name="octolytics-actor-id" /><meta content="Profshen" name="octolytics-actor-login" /><meta content="20d55085434dc6bc92d5992ff0e8feb8c632df03939e63a13105478dd6a35bc5" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="BtNIvNcxqP2PhBohbsDlbL3TRcrXiP6BVBTRSV5v1hlLch9pP5VSvF46bTGXgplLGN9PMF/zGXso4W+/HKDfSw==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-9bcf5def7eb44e2a101b20aaecf3707f4b0a10ab8f4d6eebec29371f821c4b29.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-47bc67324d463c7cecb5ee4c009628c91db85b0e9288a9e663f2d06ff9e03088.css" media="all" rel="stylesheet" type="text/css" />
    
    


    <meta http-equiv="x-pjax-version" content="cffc32e08a29062b908cc3ddb47285af">

      
  <meta name="description" content="Computational-Journalism-for-People-s-Daily-Opinion - Statistical topic models – one of the sub fields of machine learning and natural language processing – provide a data-driven framework for analyzing collections of text documents. It has become one of the most frequently used tools for computational journalism used to investigate abstract topics and keywords that occur in a collection of text documents. Digital journalists can use such tools to extract frequently appearing terms, and to analyze the trend of a particular news brand or stories about a social event. Articles, analyses and documents written in Chinese have become increasingly important for multimedia stories about China. Available Chinese archives on the Internet might contain stories that require digital journalists to apply appropriate topic modeling tools. Unlike English and other alphabetic languages, the basic structural unit of Chinese language is character encoded in Guobiao GB18030 or Unicode.  I implement apps using the Chinese topic-modeling tools jieba for computational journalism. This app analyzes articles from the opinion archive of the People’s Daily and generate a list of frequently appearing words using the keyword extraction tool provided by the jieba library.">
  <meta name="go-import" content="github.com/puconghan/Computational-Journalism-for-People-s-Daily-Opinion git https://github.com/puconghan/Computational-Journalism-for-People-s-Daily-Opinion.git">

  <meta content="1655602" name="octolytics-dimension-user_id" /><meta content="puconghan" name="octolytics-dimension-user_login" /><meta content="15912611" name="octolytics-dimension-repository_id" /><meta content="puconghan/Computational-Journalism-for-People-s-Daily-Opinion" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="15912611" name="octolytics-dimension-repository_network_root_id" /><meta content="puconghan/Computational-Journalism-for-People-s-Daily-Opinion" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/commits/master.atom" rel="alternate" title="Recent Commits to Computational-Journalism-for-People-s-Daily-Opinion:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production macintosh vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" ga-data-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>
      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item explore">
          <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
          </li>
        <li class="header-nav-item">
          <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
        </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/Profshen" data-ga-click="Header, go to profile, text:username">
      <img alt="Profshen" class="avatar" data-user="6202843" height="20" src="https://avatars2.githubusercontent.com/u/6202843?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">Profshen</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="#" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      
<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="dropdown-divider"></li>
    <li class="dropdown-header">
      <span title="puconghan/Computational-Journalism-for-People-s-Daily-Opinion">This repository</span>
    </li>
      <li>
        <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
</ul>

    </div>
  </li>

  <li class="header-nav-item">
        <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
        <span class="mail-status all-read"></span>
        <span class="octicon octicon-inbox"></span>
</a>
  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="pIKgrqKgU9svi45bNpHH5kJdZpmm8OXhfqoVmnG3PEezXtoEZQ/QaxrW9/5zwnfQY4OfVRQSb7OrRZf73JyDzQ==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>


    
  </div>
</div>

      

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="G9uvbE9T5BXmzgdFDrdHd5CHiSJPcoaop0bE+SNsvLlJIuYIKm2s8mNTcynBBvONRQx95HalGLFToUT3o1b3Ww==" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="15912611" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/watchers">
        1
      </a>
      <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/subscription"
        class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
        <span class="js-select-button">
          <span class="octicon octicon-eye"></span>
          Watch
        </span>
      </a>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
            <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">Be notified when participating or @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">Be notified of all conversations.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">Never be notified.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="sW5cXgvVQ2HhheLQUhOtSbPA1EUu8PvEdOBaVSTyZ/xp1mkCendTzheKPU6hc1pqPBLFIi8YFXadNk2UF2Uavg==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Unstar this repository" title="Unstar puconghan/Computational-Journalism-for-People-s-Daily-Opinion">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="3NwbXce+7nx4d4oqQ+zixabzZPPHBpIzx9I41ULSuFwvBfXBuiAzWw70njVM1tmdPlEJgg0z7u0Vei9rCyiBaA==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Star this repository" title="Star puconghan/Computational-Journalism-for-People-s-Daily-Opinion">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/stargazers">
          0
        </a>
</form>  </div>

  </li>


        <li>
          <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/fork" class="minibutton with-count js-toggler-target fork-button tooltipped-n" title="Fork your own copy of puconghan/Computational-Journalism-for-People-s-Daily-Opinion to your account" aria-label="Fork your own copy of puconghan/Computational-Journalism-for-People-s-Daily-Opinion to your account" rel="nofollow" data-method="post">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/network" class="social-count">0</a>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/puconghan" class="url fn" itemprop="url" rel="author"><span itemprop="title">puconghan</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion" class="js-current-repository" data-pjax="#js-repo-pjax-container">Computational-Journalism-for-People-s-Daily-Opinion</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /puconghan/Computational-Journalism-for-People-s-Daily-Opinion">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /puconghan/Computational-Journalism-for-People-s-Daily-Opinion/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
      <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /puconghan/Computational-Journalism-for-People-s-Daily-Opinion/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>


      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /puconghan/Computational-Journalism-for-People-s-Daily-Opinion/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /puconghan/Computational-Journalism-for-People-s-Daily-Opinion/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /puconghan/Computational-Journalism-for-People-s-Daily-Opinion/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                
  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/puconghan/Computational-Journalism-for-People-s-Daily-Opinion.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:puconghan/Computational-Journalism-for-People-s-Daily-Opinion.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/puconghan/Computational-Journalism-for-People-s-Daily-Opinion" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>, <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>, or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>

  <a href="http://mac.github.com" data-url="github-mac://openRepo/https://github.com/puconghan/Computational-Journalism-for-People-s-Daily-Opinion" class="minibutton sidebar-button js-conduit-rewrite-url" title="Save puconghan/Computational-Journalism-for-People-s-Daily-Opinion to your computer and use it in GitHub Desktop." aria-label="Save puconghan/Computational-Journalism-for-People-s-Daily-Opinion to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>


                <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download the contents of puconghan/Computational-Journalism-for-People-s-Daily-Opinion as a zip file"
                   title="Download the contents of puconghan/Computational-Journalism-for-People-s-Daily-Opinion as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/blob/fe004612e41f6eef121dfa561c9d345f02bf9338/jieba_analysis/PeoplesDaily_Jieba_all_TFIDF.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:31e6d619c00ef7fb5b7d042cacbdb373 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/blob/master/jieba_analysis/PeoplesDaily_Jieba_all_TFIDF.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Computational-Journalism-for-People-s-Daily-Opinion</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/tree/master/jieba_analysis" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">jieba_analysis</span></a></span><span class="separator">/</span><strong class="final-path">PeoplesDaily_Jieba_all_TFIDF.py</strong>
  </div>
</div>

<include-fragment class="commit commit-loader file-history-tease" src="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/contributors/master/jieba_analysis/PeoplesDaily_Jieba_all_TFIDF.py">
  <div class="file-history-tease-header">
    Fetching contributors&hellip;
  </div>

  <div class="participation">
    <p class="loader-loading"><img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
    <p class="loader-error">Cannot retrieve contributors at this time</p>
  </div>
</include-fragment>
<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
          <span>19 lines (16 sloc)</span>
          <span class="meta-divider"></span>
        <span>0.488 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
          <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/raw/master/jieba_analysis/PeoplesDaily_Jieba_all_TFIDF.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/blame/master/jieba_analysis/PeoplesDaily_Jieba_all_TFIDF.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/commits/master/jieba_analysis/PeoplesDaily_Jieba_all_TFIDF.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

          <a class="octicon-button tooltipped tooltipped-nw js-conduit-openfile-check"
             href="http://mac.github.com"
             data-url="github-mac://openRepo/https://github.com/puconghan/Computational-Journalism-for-People-s-Daily-Opinion?branch=master&amp;filepath=jieba_analysis%2FPeoplesDaily_Jieba_all_TFIDF.py"
             aria-label="Open this file in GitHub for Mac"
             data-failed-title="Your version of GitHub for Mac is too old to open this file. Try checking for updates.">
              <span class="octicon octicon-device-desktop"></span>
          </a>

              <a class="octicon-button tooltipped tooltipped-n js-update-url-with-hash"
                 aria-label="Clicking this button will fork this project so you can edit the file"
                 href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/edit/master/jieba_analysis/PeoplesDaily_Jieba_all_TFIDF.py"
                 data-method="post" rel="nofollow"><span class="octicon octicon-pencil"></span></a>

            <a class="octicon-button danger tooltipped tooltipped-s"
               href="/puconghan/Computational-Journalism-for-People-s-Daily-Opinion/delete/master/jieba_analysis/PeoplesDaily_Jieba_all_TFIDF.py"
               aria-label="Fork this project and delete file"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">
          <span class="octicon octicon-trashcan"></span>
        </a>
      </div><!-- /.actions -->
    </div>
    

  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line"><span class="pl-c">#encoding=utf-8</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line"><span class="pl-k">import</span> jieba</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line"><span class="pl-k">import</span> jieba.analyse</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line"><span class="pl-k">import</span> csv</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line">jieba.load_userdict(<span class="pl-s1"><span class="pl-pds">&quot;</span>customized_dict.txt<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line">TFIDF <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line">all_text <span class="pl-k">=</span> <span class="pl-s1"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line">reader <span class="pl-k">=</span> csv.reader(<span class="pl-s3">open</span>(<span class="pl-s1"><span class="pl-pds">&quot;</span>results/segmentation-jieba-result.csv<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>rb<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line"><span class="pl-k">for</span> line <span class="pl-k">in</span> reader:</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line">	<span class="pl-k">for</span> word <span class="pl-k">in</span> line:</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line">		all_text <span class="pl-k">=</span> all_text <span class="pl-k">+</span> word</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line"><span class="pl-k">for</span> item <span class="pl-k">in</span> jieba.analyse.extract_tags(all_text, <span class="pl-c1">20</span>):</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line">		TFIDF.append(item.encode(<span class="pl-s1"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line"><span class="pl-k">with</span> <span class="pl-s3">open</span>(<span class="pl-s1"><span class="pl-pds">&quot;</span>results/tfidf-jieba-all-result.csv<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line">	writer <span class="pl-k">=</span> csv.writer(f)</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line">	writer.writerow(TFIDF)</td>
      </tr>
</table>

  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="https://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.04660s from github-fe142-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-fc447938e306b7b2c26a33cfee9dfda9052aeb1aa6ad84b72f1b35fd008efe9e.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-56c56f7fe2ed90ca50b9eefebccd56f3b9729a85d7ba17f0f9c9ebd02f20a7e3.js" type="text/javascript"></script>
      
      
  </body>
</html>

