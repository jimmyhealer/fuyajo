<template>
  <Row type="flex" justify="space-around">
    <Col :span="22">
    <Panel shadow :padding="10">
      <div slot="title">
        <template v-if="listVisible">
          <div>
            文章列表
          </div>
        </template>
        <template v-else>
          <div>
            {{announcement.title}}
          </div>
        </template>
      </div>
      <div slot="extra">
        <Button v-if="listVisible" type="info" @click="init" :loading="btnLoading">{{$t('m.Refresh')}}</Button>
        <Button v-else type="ghost" icon="ios-undo" @click="goBack">{{$t('m.Back')}}</Button>
      </div>
      <transition-group name="announcement-animate" mode="in-out">
        <div class="no-announcement" v-if="!announcements.length" key="no-announcement">
          <p>{{$t('m.No_Announcements')}}</p>
        </div>
        <template v-if="listVisible">
          <ul class="announcements-container" key="list">
            <li v-for="announcement in announcements" :key="announcement.title">
              <div class="flex-container">
                <div class="title"><a class="entry" @click="goAnnouncement(announcement)">
                  {{announcement.title}}</a></div>
                  <!-- todo localtime to format -->
                <div class="date">{{announcement.create_time | dateformat }}</div>
                <div class="creator"> {{$t('m.By')}} {{announcement.created_by.username}}</div>
              </div>
            </li>
          </ul>
          <Pagination key="page"
                      :total="total"
                      :page-size="limit"
                      @on-change="getArticleList">
          </Pagination>
        </template>
        <template v-else>         
          <div v-katex v-highlight v-html="announcement.content" key="content" class="content-container markdown-body"></div>
        </template>
      </transition-group>
      </Panel>
    </Col>
  </Row>
</template>

<script>
  import api from '@oj/api'
  import Pagination from '@oj/components/Pagination'

  export default {
    name: 'Announcement',
    components: {
      Pagination
    },
    filters: {
      dateformat: function (value) {
        var newDate = value.split('-')
        var newDateDay = newDate[2].split('T')[0]
        return `${newDate[0]}/${newDate[1]}/${newDateDay}`
      }
    },
    data () {
      return {
        limit: 10,
        total: 10,
        btnLoading: false,
        announcements: [],
        announcement: '',
        listVisible: true
      }
    },
    mounted () {
      this.init()
    },
    methods: {
      init () {
        this.getArticleList()
      },
      getArticleList (page = 1) {
        this.btnLoading = true
        api.getArticleList((page - 1) * this.limit, this.limit).then(res => {
          this.btnLoading = false
          this.announcements = res.data.data.results
          this.total = res.data.data.total
        }, () => {
          this.btnLoading = false
        })
      },
      goAnnouncement (announcement) {
        this.announcement = announcement
        this.listVisible = false
      },
      goBack () {
        this.listVisible = true
        this.announcement = ''
      }
    },
    computed: {
    }
  }
</script>

<style scoped lang="less">
  .announcements-container {
    margin-top: -10px;
    margin-bottom: 10px;
    li {
      padding-top: 15px;
      list-style: none;
      padding-bottom: 15px;
      margin-left: 20px;
      font-size: 16px;
      border-bottom: 1px solid rgba(187, 187, 187, 0.5);
      &:last-child {
        border-bottom: none;
      }
      .flex-container {
        .title {
          flex: 1 1;
          text-align: left;
          padding-left: 10px;
          a.entry {
            color: #495060;
            &:hover {
              color: #2d8cf0;
              border-bottom: 1px solid #2d8cf0;
            }
          }
        }
        .creator {
          flex: none;
          width: 200px;
          text-align: center;
        }
        .date {
          flex: none;
          width: 200px;
          text-align: center;
        }
      }
    }
  }

  .content-container {
    padding: 0 20px 20px 20px;
  }

  .no-announcement {
    text-align: center;
    font-size: 16px;
  }changeLocale

  .announcement-animate-enter-active {
    animation: fadeIn 1s;
  }

  // highlight.js;
  /deep/ .hljs-ln-numbers {
    -webkit-touch-callout: none;
    user-select: none;

    text-align: center;
    color: #ccc;
    border-right: 1.5px solid #CCC !important;
    vertical-align: top;
    padding-right: 2px;

  }

  /deep/ .hljs-ln-code {
    padding-left: 10px !important;
  }

  /deep/ .markdown-body table{
    border: none;
    margin: 5px;
    max-width: 90%;

    /deep/ & td{
      border: none;
    }
  }
</style>
