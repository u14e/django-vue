<template>
  <div class="home-page">
    <header>
      <div class="school-name">嘉泰小学</div>
      <div class="class-name">3年2班</div>
    </header>

    <div class="subjects shadow">
      <div class="subject-line">
        <div class="subject">
          <div class="subject-icon"></div>
          <div class="subject-title">相册</div>
        </div>
        <div class="subject">
          <div class="subject-icon"><span class="notication"></span></div>
          <div class="subject-title">作业</div>
        </div>
        <div class="subject">
          <div class="subject-icon"><span class="notication"></span></div>
          <div class="subject-title">通知</div>
        </div>
        <div class="subject">
          <div class="subject-icon"></div>
          <div class="subject-title">考勤</div>
        </div>
        <div class="subject">
          <div class="subject-icon"></div>
          <div class="subject-title">校车</div>
        </div>
      </div>
      <div class="subject-line">
        <div class="subject">
          <div class="subject-icon"></div>
          <div class="subject-title">班级风采</div>
        </div>
        <div class="subject">
          <div class="subject-icon"></div>
          <div class="subject-title">竞技场</div>
        </div>
        <div class="subject">
          <div class="subject-icon"></div>
          <div class="subject-title">学生评价</div>
        </div>
        <div class="subject">
          <div class="subject-icon"></div>
          <div class="subject-title">校园公告</div>
        </div>
        <div class="subject">
          <div class="subject-icon"></div>
          <div class="subject-title">更多</div>
        </div>
      </div>
    </div>

    <div class="tabs-wrapper shadow">
      <tabs>
        <tab title="重要通知" :selected="true">
          <div class="notication-wrapper">
            <div class="notication-header">
              <div class="title">红色预警</div>
              <div class="date">2018.5.10</div>
            </div>
            <div class="notication-content">
              <p>红色暴雨预警，今天继续上班</p>
              <p>红色暴雨预警，今天继续上班</p>
              <p>红色暴雨预警，今天继续上班</p>
              <p>红色暴雨预警，今天继续上班</p>
            </div>
          </div>
        </tab>
        <tab title="校园咨询" :hasNotication="true">
          弄VS
        </tab>
        <tab title="班级课程表">
          VS今年是v你
        </tab>
      </tabs>
    </div>
  </div>
</template>

<script>
import { Tabs, Tab } from '@/components/tabs'
export default {
  data () {
    return {}
  },
  components: {
    Tabs,
    Tab
  }
}
</script>

<style lang="scss" scoped>
.home-page {
  header {
    width: 100%;
    height: 250px;
    overflow: hidden;
    background: #83ca68;
    .school-name,
    .class-name {
      margin: 30px 0 0 30px;
      font-size: 2rem;
      color: #efefef;
    }
  }
  .subjects {
    position: relative;
    margin: -40px 10px 15px;
    background: #fff;
    border-radius: 6px;
    .subject-line {
      display: flex;
      align-items: center;
      .subject {
        flex: 1;
        padding: 10px 0;
        text-align: center;
        font-size: 14px;
        .subject-icon {
          display: inline-block;
          position: relative;
          margin-bottom: 5px;
          width: 22px;
          height: 22px;
          background: #83ca68;
        }
      }
    }
  }
  .tabs-wrapper {
    position: relative;
    margin: 15px;
    background: #fff;
    border-radius: 6px;
  }
  .notication-wrapper {
    .notication-header {
      border-left: 3px solid yellow;
      padding-left: 5px;
      .title {
        font-size: 1.2rem;
      }
      .date {
        font-size: 14px;
      }
    }
    .notication-content {
      padding: 20px 10px;
      & > p {
        font-size: 14px;
      }
    }
  }
}
</style>
