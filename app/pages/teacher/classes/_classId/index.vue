<template>
    <main>
        <section class="hero is-primary is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title" v-if="classData">
                        {{classData.name}}
                    </h1>
                    <h2 class="subtitle">
                        Class overview and student reports.
                    </h2>
                </div>
            </div>
        </section>
        <section class="container stats-container">
            <div class="columns">
                <div class="column">
                    <div class="box">
                        <class-line-chart :chartData="getClassChartData" />
                    </div>
                </div>
            </div>
        </section>

        <section class="container" v-if="classData">
            <b-table
                class="box"
                :data="students"
                :bordered="false"
                :striped="true"
                :narrowed="false"
                :hoverable="true"
                :loading="!classData"
                :mobile-cards="true"
                selectable
                @select="goToStudent">

                <template slot-scope="props">
                    <b-table-column field="email" label="Email" >
                        {{ props.row.email }}
                    </b-table-column>

                    <b-table-column field="name" label="Name">
                        {{ props.row.name }}
                    </b-table-column>

                    <b-table-column field="date" label="Last activity" centered>
                        <span class="tag is-success">
                            {{ new Date(props.row.lastSignInTime).toLocaleDateString() }}
                        </span>
                    </b-table-column>

                    <b-table-column label="Points" numeric>
                        {{ props.row.points }}
                    </b-table-column>
                </template>

                <template slot="empty">
                    <section class="section">
                        <div class="content has-text-grey has-text-centered">
                            <p>
                                <b-icon
                                    icon="emoticon-sad"
                                    size="is-large">
                                </b-icon>
                            </p>
                            <p>Nothing here.</p>
                        </div>
                    </section>
                </template>
            </b-table>
        </section>
    </main>
</template>

<style scoped>
.stats-container {
    margin-top: 1rem;
    margin-bottom: 1rem;
}
</style>


<script>
import firestore from '@/services/firestore';
import ClassLineChart from '@/components/ClassLineChart';


export default {
  layout: 'teacher',
  components: {
    ClassLineChart
  },
  data () {
    return {
        classId: '',
        classData: null,
        students: null,
    };
  },
  mounted() {
    this.classId = this.$route.params.classId
    this.fetchClass();
  },
  computed: {
    getClassChartData() {
        return {
            labels: [
                'Wednesday, 28 Nov 2018',
                'Thursday, 29 Nov 2018',
                'Friday, 30 Nov 2018',
                'Saturday, 1 Dec 2018',
                'Sunday, 2 Dec 2018'
            ],
            datasets: [
                {
                    label: 'Cummulative points',
                    backgroundColor: '#209cee',
                    data: [24, 25, 16, 13, 8],
                },
                {
                    label: 'Quests attempted',
                    backgroundColor: '#00d1b2',
                    data: [38, 33, 39, 24, 13],
                }
            ]
        }
    }
  },
  methods: {
      fetchClass() {
        firestore.collection('classes').doc(this.classId).get().then(doc => {
            this.classData = {id:doc.id, ...doc.data()};
            if (this.classData.students) {
                this.students = [];
                this.classData.students.map(studentRef => studentRef.get().then(studentDoc => {
                    this.students.push({id: studentRef.id, ...studentDoc.data()});
                }));
            }
        });
      },
      goToStudent(item) {
          this.$router.push(`/teacher/classes/${this.classData.id}/students/${item.id}`);
      }
  }
};
</script>
